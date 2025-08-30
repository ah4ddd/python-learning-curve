import os
import shutil
from pathlib import Path

def rename_files(path, prefix):
    """
    Rename all files in the specified directory with a given prefix.

    Args:
        path (str): Directory path containing files to rename
        prefix (str): Prefix to add to renamed files
    """
    # Validate path
    if not os.path.exists(path):
        raise FileNotFoundError(f"Directory not found: {path}")

    if not os.path.isdir(path):
        raise NotADirectoryError(f"Path is not a directory: {path}")

    # Get all files (not directories)
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    if not files:
        print(f"⚠️  No files found in directory: {path}")
        return

    print(f"🔄 Renaming {len(files)} files in {path}")

    renamed_count = 0
    for index, filename in enumerate(files, 1):
        try:
            old_path = os.path.join(path, filename)

            # Get file extension
            file_ext = os.path.splitext(filename)[1]

            # Create new filename with zero-padded index
            new_name = f"{prefix}_{index:03d}{file_ext}"
            new_path = os.path.join(path, new_name)

            # Check if target file already exists
            if os.path.exists(new_path):
                print(f"⚠️  Skipping {filename}: Target {new_name} already exists")
                continue

            # Rename the file
            shutil.move(old_path, new_path)
            print(f"✅ {filename} → {new_name}")
            renamed_count += 1

        except Exception as e:
            print(f"❌ Error renaming {filename}: {e}")

    print(f"✨ Successfully renamed {renamed_count} out of {len(files)} files")

def create_backup(path, backup_suffix="_backup"):
    """
    Create a backup of files before renaming (optional utility function)
    """
    backup_dir = f"{path}{backup_suffix}"

    if os.path.exists(backup_dir):
        print(f"⚠️  Backup directory already exists: {backup_dir}")
        return False

    try:
        shutil.copytree(path, backup_dir)
        print(f"💾 Backup created: {backup_dir}")
        return True
    except Exception as e:
        print(f"❌ Error creating backup: {e}")
        return False
