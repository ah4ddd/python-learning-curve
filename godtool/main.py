import argparse
from utils import file_ops, youtube_ops, pdf_ops, email_ops
from utils import web_ops

def main():
    parser = argparse.ArgumentParser(description="GodTool - Automate boring digital life tasks")
    subparsers = parser.add_subparsers(dest="command")

    # File renamer
    file_parser = subparsers.add_parser("rename", help="Rename files in a directory")
    file_parser.add_argument("path", help="Directory path")
    file_parser.add_argument("prefix", help="Prefix for renamed files")

    # YouTube downloader
    yt_parser = subparsers.add_parser("yt", help="Download YouTube video")
    yt_parser.add_argument("url", help="YouTube video URL")
    yt_parser.add_argument("path", nargs='?', default='.', help="Download directory")

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

    args = parser.parse_args()

    if args.command == "rename":
        file_ops.rename_files(args.path, args.prefix)

    elif args.command == "yt":
        youtube_ops.download_video(args.url, args.path)

    elif args.command == "pdfmerge":
        pdf_ops.merge_pdfs(args.path, args.output)

    elif args.command == "sortemail":
        email_ops.sort_emails_by_sender(args.sender)

    elif args.command == "fetch":
        print(web_ops.pretty_fetch(args.url, args.lines))

if __name__ == "__main__":
    main()
