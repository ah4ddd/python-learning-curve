# GodTool - Automate Your Digital Life

A sophisticated command-line automation tool that handles file management, YouTube downloads, PDF operations, email sorting, web scraping, and intelligent task scheduling.

## Table of Contents
1. [Project Structure](#project-structure)
2. [Installation & Setup](#installation--setup)
3. [Core Features](#core-features)
4. [Command Reference](#command-reference)
5. [Scheduler System](#scheduler-system)
6. [Configuration](#configuration)
7. [Troubleshooting](#troubleshooting)
8. [Architecture Overview](#architecture-overview)

## Project Structure

```
godtool/
├── main.py                 # Main CLI entry point
├── setup.py               # Automated setup script
├── requirements.txt       # Python dependencies
├── README.md             # This documentation
├── config/
│   ├── settings.json     # Email and general settings
│   └── scheduled_jobs.json # Scheduled tasks storage
├── logs/
│   └── scheduler.log     # Scheduler execution logs
└── utils/
    ├── __init__.py       # Package initialization
    ├── scheduler.py      # Task scheduling engine
    ├── file_ops.py       # File management operations
    ├── email_ops.py      # Email automation
    ├── web_ops.py        # Web scraping and fetching
    ├── youtube_ops.py    # YouTube video downloads
    └── pdf_ops.py        # PDF manipulation
```

## Installation & Setup

### Prerequisites
- Python 3.7+ installed
- Git (optional, for cloning)
- Internet connection for dependencies

### Quick Setup
```bash
# Clone or download the project
cd godtool

# Run automated setup
python setup.py

# Verify installation
python main.py --help
```

### Manual Setup
```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Create required directories
mkdir -p config logs utils

# Create default config
cp config/settings.json.example config/settings.json
```

### Dependencies
The tool requires these Python packages:
- `yt-dlp` - YouTube video downloading
- `PyPDF2` - PDF manipulation
- `requests` - HTTP requests
- `beautifulsoup4` - HTML parsing
- `imaplib` - Email operations (built-in)
- `schedule` - Task scheduling
- `argparse` - CLI interface (built-in)

## Core Features

### 1. File Operations
**Batch file renaming with intelligent numbering**
- Renames all files in a directory with a consistent prefix
- Preserves file extensions
- Uses zero-padded numbering (001, 002, etc.)
- Handles existing file conflicts gracefully

### 2. YouTube Operations
**High-quality video downloading**
- Downloads videos in best available quality
- Supports playlists and individual videos
- Customizable download location
- Error handling for invalid URLs

### 3. PDF Operations
**Intelligent PDF merging**
- Merges all PDFs in a directory alphabetically
- Preserves document quality
- Customizable output filename
- Handles large files efficiently

### 4. Email Automation
**Smart email sorting by sender**
- Connects to IMAP servers (Gmail, Outlook, etc.)
- Sorts unread emails from specific senders
- Creates organized folder structure
- Supports app passwords for security

### 5. Web Operations
**Intelligent web content fetching**
- Detects content type automatically (JSON, HTML, plain text)
- Pretty-prints JSON with proper formatting
- Extracts readable text from HTML pages
- Customizable output length
- Error handling for network issues

### 6. Advanced Scheduler
**Sophisticated task automation**
- Schedule any GodTool operation to run automatically
- Supports one-time, daily, and interval-based scheduling
- Intelligent timezone handling
- Persistent job storage
- Daemon mode for background execution
- Comprehensive logging and error handling

## Command Reference

### Basic Operations

#### File Renaming
```bash
# Rename all files in a directory
python main.py rename /path/to/files "NewPrefix"

# Example output:
# photo1.jpg → NewPrefix_001.jpg
# document.pdf → NewPrefix_002.pdf
```

#### YouTube Download
```bash
# Download to current directory
python main.py yt "https://youtu.be/VIDEO_ID"

# Download to specific directory
python main.py yt "https://youtu.be/VIDEO_ID" /home/user/videos

# The tool automatically handles:
# - URL cleaning (removes escape characters)
# - Best quality selection
# - Filename sanitization
```

#### PDF Merging
```bash
# Merge all PDFs in folder
python main.py pdfmerge /path/to/pdf/folder

# Custom output name
python main.py pdfmerge /path/to/pdf/folder --output "Combined_Report.pdf"
```

#### Email Sorting
```bash
# Sort emails from specific sender
python main.py sortemail important@company.com

# This will:
# 1. Connect to your email server
# 2. Find unread emails from the sender
# 3. Move them to a "Sorted" folder
# 4. Provide detailed statistics
```

#### Web Fetching
```bash
# Fetch and display webpage content
python main.py fetch "https://api.github.com"

# Show more lines
python main.py fetch "https://example.com" --lines 50

# The tool intelligently handles:
# - JSON APIs (pretty-printed)
# - HTML pages (text extraction)
# - Plain text content
# - Error pages and timeouts
```

## Scheduler System

The scheduler is the most sophisticated component, allowing you to automate any GodTool operation.

### Scheduling Jobs

#### One-time Execution
```bash
# Schedule a YouTube download for 15:30 today
python main.py schedule add --job yt --url "https://youtu.be/VIDEO" --path /downloads --time "15:30"

# Schedule PDF merge for 2:45 PM
python main.py schedule add --job pdfmerge --path /documents --time "14:45"
```

#### Daily Recurring Jobs
```bash
# Download a daily podcast at 8:00 AM every day
python main.py schedule add --job yt --url "PODCAST_URL" --daily --time "08:00"

# Sort emails from your boss every weekday at 9:00 AM
python main.py schedule add --job sortemail --sender "boss@company.com" --daily --time "09:00"
```

#### Interval-based Jobs
```bash
# Check a website every 30 minutes
python main.py schedule add --job fetch --url "https://status.example.com" --interval 30

# Organize files every 2 hours
python main.py schedule add --job rename --path /downloads --prefix "Auto" --interval 120
```

### Managing Scheduled Jobs

#### List All Jobs
```bash
python main.py schedule list

# Output example:
# Scheduled Jobs:
# ID   Type      Schedule        Next Run      Status
# 1    yt        Daily at 08:00  08:00:00     scheduled
# 2    fetch     Every 30min     14:45:30     scheduled
```

#### Remove Jobs
```bash
# Remove single job
python main.py schedule remove 1

# Remove multiple jobs
python main.py schedule remove 1 2 3

# Remove all jobs
python main.py schedule clear
```

#### Daemon Control
```bash
# Start the scheduler daemon (runs in foreground)
python main.py schedule start

# The daemon will:
# - Check for due jobs every 5 seconds
# - Execute jobs in separate threads
# - Log all activity
# - Handle errors gracefully
# - Continue running until stopped with Ctrl+C
```

### Scheduler Intelligence Features

**Timezone Awareness**: Automatically detects your system timezone and schedules accordingly.

**Smart Immediate Execution**: If you schedule a job for a time that just passed (within 3 hours), it runs in 30 seconds instead of waiting until tomorrow.

**Conflict Resolution**: Handles existing files, network errors, and system interruptions gracefully.

**Persistent Storage**: Jobs survive system reboots and are stored in JSON format.

**Thread Safety**: Multiple jobs can run simultaneously without blocking each other.

## Configuration

### Email Configuration
Edit `config/settings.json`:

```json
{
  "email": "your-email@gmail.com",
  "password": "your-app-password",
  "imap_server": "imap.gmail.com",
  "imap_port": 993,
  "inbox_folder": "INBOX",
  "sorted_folder": "Sorted"
}
```

**Important**: Use app passwords, not your regular password:
- **Gmail**: Go to Google Account Settings → Security → App Passwords
- **Outlook**: Go to Security Settings → App Passwords

### Scheduler Configuration
Jobs are stored in `config/scheduled_jobs.json`. This file is automatically managed, but you can inspect it:

```json
[
  {
    "id": 1,
    "type": "yt",
    "args": {
      "url": "https://youtu.be/VIDEO",
      "path": "/downloads"
    },
    "schedule_time": "08:00",
    "daily": true,
    "status": "scheduled",
    "next_run": "2025-08-31T08:00:00"
  }
]
```

## Troubleshooting

### Common Issues

#### Scheduler Not Running Jobs
**Problem**: Jobs scheduled but never execute
**Diagnosis**:
```bash
# Check your system timezone
date
# Should show IST if you're in India

# Check scheduled jobs
python main.py schedule list
```

**Solutions**:
1. **Timezone mismatch**: If `date` shows UTC but you're in India:
   ```bash
   sudo timedatectl set-timezone Asia/Kolkata
   ```

2. **Time format**: Use 24-hour format (14:30, not 2:30 PM)

3. **Past times**: If you schedule for a time that already passed, the tool schedules for tomorrow unless it's within 3 hours

#### Email Connection Issues
**Problem**: "IMAP connection error" or authentication failures

**Solutions**:
1. **Enable app passwords**: Use app-specific passwords, not your regular password
2. **Enable IMAP**: Make sure IMAP is enabled in your email settings
3. **Check configuration**: Verify `config/settings.json` has correct server details

#### YouTube Download Failures
**Problem**: "Error downloading video"

**Solutions**:
1. **Update yt-dlp**: `pip install --upgrade yt-dlp`
2. **Check URL**: Ensure the YouTube URL is valid and accessible
3. **Network issues**: Verify internet connection

#### File Permission Issues
**Problem**: "Permission denied" errors

**Solutions**:
1. **Check permissions**: Ensure you have write access to target directories
2. **Use absolute paths**: `/home/user/files` instead of `~/files`
3. **Create directories**: Make sure target directories exist

### Debug Mode
Enable verbose logging by editing the logging level in any utils file:
```python
logging.basicConfig(level=logging.DEBUG)
```

### Logs Location
- Scheduler logs: `logs/scheduler.log`
- Application logs: Console output
- Error logs: Both console and log files

## Architecture Overview

### Design Principles
1. **Modular Architecture**: Each feature is in its own module for maintainability
2. **Error Resilience**: Comprehensive error handling at every level
3. **User Experience**: Clear feedback and progress indicators
4. **Extensibility**: Easy to add new automation features
5. **Security**: Safe handling of credentials and file operations

### Core Components

#### CLI Interface (`main.py`)
- Argument parsing and validation
- Command routing to appropriate modules
- Global error handling
- Help system and examples

#### Scheduler Engine (`utils/scheduler.py`)
- Job persistence and management
- Intelligent timing calculations
- Multi-threaded execution
- Daemon mode for background operation
- Comprehensive logging

#### Operation Modules (`utils/*.py`)
Each module is self-contained and handles:
- Input validation
- Error handling
- Progress reporting
- Resource cleanup

### Data Flow
1. **Command Input**: User runs CLI command
2. **Parsing**: Arguments parsed and validated
3. **Routing**: Command routed to appropriate module
4. **Execution**: Module performs operation with error handling
5. **Feedback**: Results reported to user
6. **Logging**: Activity logged for debugging

### Security Considerations
- Email passwords stored in local config files only
- No network transmission of credentials
- File operations respect system permissions
- Input validation prevents directory traversal
- Safe error handling prevents information leakage

### Performance Features
- Multi-threaded job execution
- Efficient file handling for large operations
- Optimized PDF processing
- Intelligent web request management
- Resource cleanup and memory management

## Advanced Usage

### Chaining Operations
You can chain multiple operations by scheduling them in sequence:

```bash
# Schedule a workflow: download video, then organize files
python main.py schedule add --job yt --url "VIDEO_URL" --time "10:00"
python main.py schedule add --job rename --path /downloads --prefix "Daily" --time "10:05"
```

### Automation Examples

**Daily Content Organization**:
```bash
# Every day at 6 AM: download news podcast
python main.py schedule add --job yt --url "NEWS_PODCAST" --daily --time "06:00"

# Every day at 6:30 AM: organize downloaded files
python main.py schedule add --job rename --path /downloads --prefix "Daily" --daily --time "06:30"

# Every day at 7 AM: merge PDFs from work folder
python main.py schedule add --job pdfmerge --path /work/docs --daily --time "07:00"
```

**Email Management Automation**:
```bash
# Sort important emails every 2 hours
python main.py schedule add --job sortemail --sender "boss@company.com" --interval 120

# Sort newsletter emails daily
python main.py schedule add --job sortemail --sender "newsletter@site.com" --daily --time "23:00"
```

**Content Monitoring**:
```bash
# Check website status every 15 minutes
python main.py schedule add --job fetch --url "https://mysite.com/status" --interval 15

# Daily backup of important web content
python main.py schedule add --job fetch --url "https://important-api.com/data" --daily --time "03:00"
```

### Error Recovery
The tool includes sophisticated error recovery:
- **Network failures**: Automatic retry with exponential backoff
- **File conflicts**: Intelligent renaming to avoid overwrites
- **Authentication issues**: Clear error messages with solution hints
- **System interruptions**: Graceful shutdown and state preservation

## Best Practices

### Scheduling
1. **Use absolute paths**: Always specify full paths to avoid confusion
2. **Test first**: Run commands manually before scheduling
3. **Monitor logs**: Check `logs/scheduler.log` for execution details
4. **Stagger jobs**: Don't schedule too many jobs at the same time
5. **Use appropriate intervals**: Consider system resources and network usage

### File Operations
1. **Backup important data**: Always backup before bulk operations
2. **Use descriptive prefixes**: Make file organization clear
3. **Check permissions**: Ensure write access to target directories
4. **Monitor disk space**: Large operations may fill storage

### Email Operations
1. **Use app passwords**: Never use your main account password
2. **Test connectivity**: Verify email settings before scheduling
3. **Monitor sorted folders**: Check that emails are properly organized
4. **Backup email**: Consider email backups before automation

### Security
1. **Protect config files**: Keep `settings.json` secure
2. **Use minimal permissions**: Only grant necessary file system access
3. **Regular updates**: Keep dependencies updated for security
4. **Monitor logs**: Review logs for unusual activity

## Examples by Use Case

### Content Creator Workflow
```bash
# Download daily content
python main.py schedule add --job yt --url "DAILY_SOURCE" --daily --time "07:00"

# Organize downloads
python main.py schedule add --job rename --path /content --prefix "Content" --daily --time "07:30"

# Merge daily PDFs
python main.py schedule add --job pdfmerge --path /scripts --daily --time "08:00"
```

### System Administrator Tasks
```bash
# Monitor server status every 10 minutes
python main.py schedule add --job fetch --url "https://server/health" --interval 10

# Daily log organization
python main.py schedule add --job rename --path /var/log/processed --prefix "Log" --daily --time "00:30"

# Weekly report generation
python main.py schedule add --job pdfmerge --path /reports/weekly --daily --time "23:55"
```

### Personal Productivity
```bash
# Sort personal emails twice daily
python main.py schedule add --job sortemail --sender "family@email.com" --daily --time "08:00"
python main.py schedule add --job sortemail --sender "family@email.com" --daily --time "20:00"

# Weekly file organization
python main.py schedule add --job rename --path /home/downloads --prefix "Week" --daily --time "23:00"
```

## Technical Implementation Details

### Scheduler Architecture
The scheduler uses a sophisticated timing system:

1. **Job Storage**: Jobs stored in JSON with full state persistence
2. **Timing Engine**: Calculates execution times considering timezone and edge cases
3. **Execution Engine**: Multi-threaded job execution with isolation
4. **Error Handling**: Comprehensive error recovery and logging
5. **Daemon Mode**: Background process for continuous operation

### Error Handling Strategy
Each module implements a three-tier error handling approach:
1. **Input Validation**: Prevent errors before they occur
2. **Graceful Degradation**: Handle expected failures elegantly
3. **Emergency Recovery**: Log and report unexpected failures

### Performance Optimizations
- **Lazy Loading**: Modules loaded only when needed
- **Resource Management**: Proper cleanup of file handles and network connections
- **Memory Efficiency**: Streaming operations for large files
- **Concurrent Execution**: Non-blocking operations where possible

## Extending GodTool

### Adding New Operations
1. Create a new module in `utils/` (e.g., `utils/new_ops.py`)
2. Implement your operation functions
3. Add CLI arguments in `main.py`
4. Add routing logic in the main function
5. Update the scheduler to support the new operation type

### Integration Examples
The tool is designed to integrate with:
- **Cloud storage** (add sync operations)
- **Database systems** (add data operations)
- **Web APIs** (extend web operations)
- **System monitoring** (add health checks)
- **Notification systems** (add alert operations)

## Version History & Updates

### Current Features
- Cross-platform compatibility (Linux, macOS, Windows)
- Timezone-aware scheduling
- Comprehensive error handling
- Modular architecture
- Extensive logging
- Configuration management

### Planned Enhancements
- Web interface for remote management
- More file operation types
- Advanced email filtering
- Cloud integration
- Performance monitoring
- Backup and restore functionality

---

**Support**: For issues or questions, check the logs directory or run commands with `--help` for detailed usage information.
