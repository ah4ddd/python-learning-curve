import time
import json
import os
import threading
import signal
import sys
from datetime import datetime, timedelta
import logging
import pytz
from utils import file_ops, youtube_ops, pdf_ops, email_ops, web_ops

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/scheduler.log'),
        logging.StreamHandler()
    ]
)

class JobScheduler:
    def __init__(self):
        self.jobs_file = 'config/scheduled_jobs.json'
        self.daemon_running = False
        self.jobs = self.load_jobs()
        self.job_counter = max([job.get('id', 0) for job in self.jobs], default=0) + 1

        # Ensure directories exist
        os.makedirs('config', exist_ok=True)
        os.makedirs('logs', exist_ok=True)

    def load_jobs(self):
        """Load scheduled jobs from file"""
        try:
            if os.path.exists(self.jobs_file):
                with open(self.jobs_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            logging.error(f"Error loading jobs: {e}")
        return []

    def save_jobs(self):
        """Save scheduled jobs to file"""
        try:
            with open(self.jobs_file, 'w') as f:
                json.dump(self.jobs, f, indent=2, default=str)
        except Exception as e:
            logging.error(f"Error saving jobs: {e}")

    def add_job(self, job_type, args, schedule_time=None, interval=None, daily=False):
        """Add a new scheduled job with IST timezone support"""
        # Get times in both UTC and IST
        utc_now = datetime.now()
        ist = pytz.timezone('Asia/Kolkata')
        ist_now = datetime.now(ist).replace(tzinfo=None)  # Remove timezone info for comparison

        job = {
            'id': self.job_counter,
            'type': job_type,
            'args': args,
            'schedule_time': schedule_time,
            'interval': interval,
            'daily': daily,
            'created': utc_now.isoformat(),
            'last_run': None,
            'next_run': None,
            'status': 'scheduled'
        }

        # Calculate next run time
        if interval:
            next_run = utc_now + timedelta(minutes=interval)
        elif schedule_time:
            hour, minute = map(int, schedule_time.split(':'))

            # Create the target time in IST, then convert to UTC
            ist_target = ist_now.replace(hour=hour, minute=minute, second=0, microsecond=0)

            # Convert IST to UTC (subtract 5:30)
            utc_target = ist_target - timedelta(hours=5, minutes=30)

            if utc_target <= utc_now:
                if daily:
                    # Daily job - schedule for tomorrow in IST
                    utc_target += timedelta(days=1)
                else:
                    # One-time job - if within last 3 hours IST, run in 30 seconds
                    ist_hours_passed = (ist_now - ist_target).total_seconds() / 3600
                    if ist_hours_passed <= 3:
                        utc_target = utc_now + timedelta(seconds=30)
                        print(f"IST time recently passed - running in 30 seconds")
                    else:
                        utc_target += timedelta(days=1)

            job['next_run'] = utc_target.isoformat()

        self.jobs.append(job)
        self.job_counter += 1
        self.save_jobs()

        print(f"Job {job['id']} scheduled for {job_type}")

        if job.get('next_run'):
            next_dt = datetime.fromisoformat(job['next_run'])
            # Convert back to IST for display
            ist_next = next_dt + timedelta(hours=5, minutes=30)

            print(f"IST time: {ist_now.strftime('%H:%M:%S')}")
            print(f"Will run at: {ist_next.strftime('%H:%M:%S')} IST")

            time_diff = (next_dt - utc_now).total_seconds()
            if time_diff <= 120:
                print(f"Will run in {int(time_diff)} seconds")

        return job['id']

    def remove_job(self, job_id):
        """Remove a single scheduled job"""
        original_count = len(self.jobs)
        self.jobs = [job for job in self.jobs if job.get('id') != job_id]

        if len(self.jobs) < original_count:
            self.save_jobs()
            print(f"Job {job_id} removed")
        else:
            print(f"Job {job_id} not found")

    def remove_multiple_jobs(self, job_ids):
        """Remove multiple jobs at once"""
        removed_count = 0
        not_found = []

        for job_id in job_ids:
            original_count = len(self.jobs)
            self.jobs = [job for job in self.jobs if job.get('id') != job_id]

            if len(self.jobs) < original_count:
                removed_count += 1
                print(f"Job {job_id} removed")
            else:
                not_found.append(job_id)

        if removed_count > 0:
            self.save_jobs()
            print(f"Successfully removed {removed_count} jobs")

        if not_found:
            print(f"Jobs not found: {', '.join(map(str, not_found))}")

    def clear_all_jobs(self):
        """Remove all scheduled jobs"""
        job_count = len(self.jobs)
        self.jobs = []
        self.save_jobs()
        print(f"Cleared all {job_count} jobs")

    def list_jobs(self):
        """List all scheduled jobs"""
        if not self.jobs:
            print("No scheduled jobs found")
            return

        print("\nScheduled Jobs:")
        print("-" * 70)
        print(f"{'ID':<4} {'Type':<10} {'Schedule':<15} {'Next Run':<15} {'Status':<10}")
        print("-" * 70)

        current_time = datetime.now()

        for job in self.jobs:
            job_id = str(job.get('id', 'N/A'))
            job_type = str(job.get('type', 'N/A'))
            job_status = str(job.get('status', 'N/A'))

            # Schedule info
            if job.get('daily') and job.get('schedule_time'):
                schedule_info = f"Daily {job.get('schedule_time', 'N/A')}"
            elif job.get('interval'):
                schedule_info = f"Every {job.get('interval', 'N/A')}min"
            else:
                schedule_info = "One-time"

            # Next run
            next_run_str = "N/A"
            if job.get('next_run'):
                try:
                    next_run_dt = datetime.fromisoformat(job['next_run'])
                    next_run_str = next_run_dt.strftime('%H:%M:%S')

                    if next_run_dt <= current_time and job_status == 'scheduled':
                        next_run_str += " (DUE)"
                except:
                    next_run_str = "Invalid"

            print(f"{job_id:<4} {job_type:<10} {schedule_info:<15} {next_run_str:<15} {job_status:<10}")

        print(f"\nCurrent time: {current_time.strftime('%H:%M:%S')}")

    def execute_job(self, job):
        """Execute a scheduled job"""
        try:
            print(f"\nExecuting job {job['id']} - {job['type']}")
            job['status'] = 'running'
            job['last_run'] = datetime.now().isoformat()

            if job['type'] == 'rename':
                file_ops.rename_files(job['args']['path'], job['args']['prefix'])
            elif job['type'] == 'yt':
                youtube_ops.download_video(job['args']['url'], job['args'].get('path', '.'))
            elif job['type'] == 'pdfmerge':
                pdf_ops.merge_pdfs(job['args']['path'], job['args'].get('output', 'merged.pdf'))
            elif job['type'] == 'sortemail':
                email_ops.sort_emails_by_sender(job['args']['sender'])
            elif job['type'] == 'fetch':
                result = web_ops.pretty_fetch(job['args']['url'], job['args'].get('lines', 20))
                print(result)

            # Schedule next run for recurring jobs
            if job.get('daily') and job.get('schedule_time'):
                hour, minute = map(int, job['schedule_time'].split(':'))
                next_run = datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0) + timedelta(days=1)
                job['next_run'] = next_run.isoformat()
                job['status'] = 'scheduled'
            elif job.get('interval'):
                next_run = datetime.now() + timedelta(minutes=job['interval'])
                job['next_run'] = next_run.isoformat()
                job['status'] = 'scheduled'
            else:
                job['next_run'] = None
                job['status'] = 'completed'

            print(f"Job {job['id']} completed successfully")

        except Exception as e:
            job['status'] = 'failed'
            print(f"Job {job['id']} failed: {e}")

        self.save_jobs()

    def run_daemon(self):
        """Run the scheduler daemon"""
        self.daemon_running = True
        print(f"Scheduler started at: {datetime.now().strftime('%H:%M:%S')}")

        def signal_handler(signum, frame):
            self.daemon_running = False

        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)

        while self.daemon_running:
            try:
                current_time = datetime.now()

                for job in self.jobs:
                    if job.get('status') != 'scheduled':
                        continue

                    if job.get('next_run'):
                        try:
                            next_run_time = datetime.fromisoformat(job['next_run'])

                            if current_time >= next_run_time:
                                print(f"Running job {job['id']} now")
                                thread = threading.Thread(target=self.execute_job, args=(job,))
                                thread.daemon = True
                                thread.start()

                        except:
                            continue

                time.sleep(5)  # Check every 5 seconds

            except Exception as e:
                print(f"Daemon error: {e}")
                time.sleep(30)

        print("Scheduler stopped")

# Global scheduler instance
scheduler_instance = JobScheduler()

def schedule_job(args):
    """Schedule a new job"""
    job_args = {}

    if args.job == 'rename':
        if not args.path or not args.prefix:
            raise ValueError("Rename job requires --path and --prefix arguments")
        job_args = {'path': args.path, 'prefix': args.prefix}
    elif args.job == 'yt':
        if not args.url:
            raise ValueError("YouTube job requires --url argument")
        job_args = {'url': args.url, 'path': args.path or '.'}
    elif args.job == 'pdfmerge':
        if not args.path:
            raise ValueError("PDF merge job requires --path argument")
        job_args = {'path': args.path, 'output': args.output or 'merged.pdf'}
    elif args.job == 'sortemail':
        if not args.sender:
            raise ValueError("Email sort job requires --sender argument")
        job_args = {'sender': args.sender}
    elif args.job == 'fetch':
        if not args.url:
            raise ValueError("Web fetch job requires --url argument")
        job_args = {'url': args.url, 'lines': args.lines}

    if not any([args.time, args.interval, args.daily]):
        raise ValueError("Must specify --time, --interval, or --daily for scheduling")

    if args.daily and not args.time:
        raise ValueError("Daily jobs require --time argument")

    scheduler_instance.add_job(
        job_type=args.job,
        args=job_args,
        schedule_time=args.time,
        interval=args.interval,
        daily=args.daily
    )

def list_jobs():
    scheduler_instance.list_jobs()

def remove_job(job_id):
    """Remove a single job or multiple jobs"""
    if isinstance(job_id, list):
        scheduler_instance.remove_multiple_jobs(job_id)
    else:
        scheduler_instance.remove_job(job_id)

def clear_all_jobs():
    """Remove all scheduled jobs"""
    scheduler_instance.clear_all_jobs()

def start_daemon():
    print("Starting scheduler daemon...")
    print("Press Ctrl+C to stop")
    try:
        scheduler_instance.run_daemon()
    except KeyboardInterrupt:
        print("\nScheduler stopped by user")

def stop_daemon():
    print("Use Ctrl+C to stop a running daemon")
