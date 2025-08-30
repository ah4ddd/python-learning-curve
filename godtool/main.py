import argparse
import sys
from utils import file_ops, youtube_ops, pdf_ops, email_ops, web_ops, scheduler

def main():
    parser = argparse.ArgumentParser(
        description="GodTool - Automate boring digital life tasks",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py rename /path/to/files "MyPrefix"
  python main.py yt "https://youtube.com/watch?v=..." /downloads
  python main.py pdfmerge /pdf/folder --output combined.pdf
  python main.py sortemail sender@example.com
  python main.py fetch "https://api.github.com" --lines 30
  python main.py schedule --job rename --path /files --prefix "Auto" --time "14:30"
  python main.py schedule --list
  python main.py schedule --remove 1
  python main.py schedule --remove-all 1,2,3
  python main.py schedule --clear
        """
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # File renamer
    file_parser = subparsers.add_parser("rename", help="Rename files in a directory")
    file_parser.add_argument("path", help="Directory path")
    file_parser.add_argument("prefix", help="Prefix for renamed files")

    # YouTube downloader
    yt_parser = subparsers.add_parser("yt", help="Download YouTube video")
    yt_parser.add_argument("url", help="YouTube video URL")
    yt_parser.add_argument("path", nargs='?', default='.', help="Download directory (default: current)")

    # PDF merger
    pdf_parser = subparsers.add_parser("pdfmerge", help="Merge all PDFs in a folder")
    pdf_parser.add_argument("path", help="Folder path containing PDFs")
    pdf_parser.add_argument("--output", default="merged.pdf", help="Output PDF filename (default: merged.pdf)")

    # Email sorting
    email_parser = subparsers.add_parser("sortemail", help="Sort unread emails by sender")
    email_parser.add_argument("sender", help="Email address of sender to sort")

    # Web fetching
    web_parser = subparsers.add_parser("fetch", help="Fetch webpage content")
    web_parser.add_argument("url", help="URL to fetch")
    web_parser.add_argument("--lines", type=int, default=20, help="Show first N lines (default: 20)")

    # Scheduler - CLEAN VERSION
    schedule_parser = subparsers.add_parser("schedule", help="Schedule tasks to run automatically")

    # Create subcommands for scheduler
    schedule_subparsers = schedule_parser.add_subparsers(dest="schedule_action", help="Scheduler actions")

    # List jobs
    list_parser = schedule_subparsers.add_parser("list", help="List all scheduled jobs")

    # Remove jobs
    remove_parser = schedule_subparsers.add_parser("remove", help="Remove jobs")
    remove_parser.add_argument("ids", nargs='+', type=int, help="Job ID(s) to remove")

    # Clear all jobs
    clear_parser = schedule_subparsers.add_parser("clear", help="Remove all jobs")

    # Start/stop daemon
    start_parser = schedule_subparsers.add_parser("start", help="Start scheduler daemon")
    stop_parser = schedule_subparsers.add_parser("stop", help="Stop scheduler daemon")

    # Add job
    add_parser = schedule_subparsers.add_parser("add", help="Add a new scheduled job")
    add_parser.add_argument("--job", choices=["rename", "yt", "pdfmerge", "sortemail", "fetch"],
                           required=True, help="Type of job to schedule")
    add_parser.add_argument("--time", help="Time to run (HH:MM format)")
    add_parser.add_argument("--interval", type=int, help="Run every N minutes")
    add_parser.add_argument("--daily", action="store_true", help="Run daily at specified time")

    # Job-specific arguments
    add_parser.add_argument("--path", help="Path for file operations")
    add_parser.add_argument("--prefix", help="Prefix for file renaming")
    add_parser.add_argument("--url", help="URL for YouTube or web operations")
    add_parser.add_argument("--output", help="Output filename")
    add_parser.add_argument("--sender", help="Email sender to sort")
    add_parser.add_argument("--lines", type=int, default=20, help="Lines to show for web fetch")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    try:
        if args.command == "rename":
            file_ops.rename_files(args.path, args.prefix)

        elif args.command == "yt":
            youtube_ops.download_video(args.url, args.path)

        elif args.command == "pdfmerge":
            pdf_ops.merge_pdfs(args.path, args.output)

        elif args.command == "sortemail":
            email_ops.sort_emails_by_sender(args.sender)

        elif args.command == "fetch":
            result = web_ops.pretty_fetch(args.url, args.lines)
            print(result)

        elif args.command == "schedule":
            if args.schedule_action == "list":
                scheduler.list_jobs()
            elif args.schedule_action == "remove":
                if len(args.ids) == 1:
                    scheduler.remove_job(args.ids[0])
                else:
                    scheduler.remove_job(args.ids)  # Will handle multiple
            elif args.schedule_action == "clear":
                scheduler.clear_all_jobs()
            elif args.schedule_action == "start":
                scheduler.start_daemon()
            elif args.schedule_action == "stop":
                scheduler.stop_daemon()
            elif args.schedule_action == "add":
                scheduler.schedule_job(args)
            else:
                schedule_parser.print_help()

    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
