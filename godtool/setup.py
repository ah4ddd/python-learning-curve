import os
import sys
import subprocess
import json
from pathlib import Path

def create_directories():
    """Create necessary directories"""
    directories = ['config', 'logs', 'utils']

    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Created directory: {directory}")

def install_dependencies():
    """Install required Python packages"""
    try:
        print("📦 Installing dependencies...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False
    return True

def create_config_files():
    """Create default configuration files"""

    # Create settings.json if it doesn't exist
    config_file = Path('config/settings.json')
    if not config_file.exists():
        default_config = {
            "email": "your-email@example.com",
            "password": "your-app-password",
            "imap_server": "imap.gmail.com",
            "imap_port": 993,
            "inbox_folder": "INBOX",
            "sorted_folder": "Sorted"
        }

        with open(config_file, 'w') as f:
            json.dump(default_config, f, indent=2)
        print(f"✅ Created config file: {config_file}")

    # Create empty scheduled_jobs.json
    jobs_file = Path('config/scheduled_jobs.json')
    if not jobs_file.exists():
        with open(jobs_file, 'w') as f:
            json.dump([], f)
        print(f"✅ Created jobs file: {jobs_file}")

def create_init_files():
    """Create __init__.py files for proper module imports"""
    init_file = Path('utils/__init__.py')
    if not init_file.exists():
        init_file.write_text('# GodTool utils package\n')
        print(f"✅ Created {init_file}")

def setup_godtool():
    """Main setup function"""
    print("🚀 Setting up GodTool...")
    print("=" * 50)

    # Create directories
    create_directories()

    # Create __init__.py files
    create_init_files()

    # Install dependencies
    if not install_dependencies():
        print("❌ Setup failed during dependency installation")
        return False

    # Create config files
    create_config_files()

    print("\n" + "=" * 50)
    print("✨ GodTool setup completed successfully!")
    print("\n📝 Next steps:")
    print("1. Edit config/settings.json with your email settings")
    print("2. Test the tool: python main.py --help")
    print("3. Try renaming files: python main.py rename /path/to/files 'MyPrefix'")
    print("4. Schedule tasks: python main.py schedule --help")
    print("\n💡 For email features, make sure to use app passwords for Gmail/Outlook")

    return True

if __name__ == "__main__":
    if not setup_godtool():
        sys.exit(1)
