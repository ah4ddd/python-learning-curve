"""
Debug script to test scheduler timing
Run this to verify your scheduler is working correctly
"""

import sys
import os
from datetime import datetime, timedelta

# Add the parent directory to path so we can import utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.scheduler import scheduler_instance

def test_immediate_execution():
    """Test scheduling a job that should run immediately"""
    print("🧪 Testing immediate job execution...")

    current_time = datetime.now()
    # Schedule for 1 minute from now
    test_time = current_time + timedelta(minutes=1)

    print(f"🕐 Current time: {current_time.strftime('%H:%M:%S')}")
    print(f"⏰ Scheduling test job for: {test_time.strftime('%H:%M:%S')}")

    # Create a simple test job (file rename)
    test_args = {
        'path': '/tmp',  # Use a safe directory
        'prefix': 'test'
    }

    job_id = scheduler_instance.add_job(
        job_type='rename',
        args=test_args,
        schedule_time=test_time.strftime('%H:%M'),
        daily=False
    )

    print(f"✅ Test job {job_id} scheduled!")
    print("💡 Now run: python main.py schedule --start")
    print("   The job should execute within 1-2 minutes")

def show_current_jobs():
    """Show all current jobs with timing details"""
    print("📋 Current Jobs Analysis:")
    print("=" * 60)

    current_time = datetime.now()
    print(f"🕐 System time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

    if not scheduler_instance.jobs:
        print("📝 No jobs found")
        return

    for job in scheduler_instance.jobs:
        print(f"\n📌 Job {job['id']} ({job['type']}):")
        print(f"   Status: {job['status']}")

        if job.get('next_run'):
            try:
                next_run = datetime.fromisoformat(job['next_run'])
                print(f"   Next run: {next_run.strftime('%Y-%m-%d %H:%M:%S')}")

                time_diff = (next_run - current_time).total_seconds()
                if time_diff > 0:
                    print(f"   ⏳ Time until execution: {int(time_diff)} seconds")
                else:
                    print(f"   🚨 OVERDUE by {int(abs(time_diff))} seconds!")
            except:
                print(f"   ❌ Invalid next_run format: {job['next_run']}")

        if job.get('schedule_time'):
            print(f"   Schedule: {job['schedule_time']} {'(daily)' if job.get('daily') else '(one-time)'}")

def quick_test():
    """Schedule a job for 30 seconds from now"""
    print("⚡ Quick Test: Scheduling job for 30 seconds from now...")

    current_time = datetime.now()
    test_time = current_time + timedelta(seconds=30)

    # Use web fetch as it's a simple, safe operation
    test_args = {
        'url': 'https://httpbin.org/json',
        'lines': 5
    }

    job_id = scheduler_instance.add_job(
        job_type='fetch',
        args=test_args,
        schedule_time=test_time.strftime('%H:%M'),
        daily=False
    )

    print(f"✅ Quick test job {job_id} scheduled for {test_time.strftime('%H:%M:%S')}")
    print("🏃 Now quickly run: python main.py schedule --start")
    print("   You should see execution within 30-40 seconds")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            test_immediate_execution()
        elif sys.argv[1] == 'quick':
            quick_test()
        elif sys.argv[1] == 'show':
            show_current_jobs()
        else:
            print("Usage: python debug_scheduler.py [test|quick|show]")
    else:
        print("🔧 GodTool Scheduler Debug")
        print("=" * 40)
        print("Commands:")
        print("  python debug_scheduler.py test  - Schedule 1-minute test")
        print("  python debug_scheduler.py quick - Schedule 30-second test")
        print("  python debug_scheduler.py show  - Show current jobs")
        print()
        show_current_jobs()
