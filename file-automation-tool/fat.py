import os
import shutil

folder_path = "./my_folder"

def backup_files(path, backup_folder):
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    for root, _, files in os.walk(path):
        for filename in files:
            file_path = os.path.join(root, filename)
            shutil.copy(file_path, os.path.join(backup_folder, filename))

def organize_files(path):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            ext = filename.split('.')[-1]
            ext_folder = os.path.join(path, ext)
            if not os.path.exists(ext_folder):
                os.makedirs(ext_folder)
            shutil.move(file_path, os.path.join(ext_folder, filename))

def rename_files_recursive(path, prefix):
    count = 1
    for root, _, files in os.walk(path):
        for filename in files:
            ext = filename.split('.')[-1]
            old_path = os.path.join(root, filename)
            new_name = f"{prefix}_{count}.{ext}"
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)
            count += 1

backup_files(folder_path, "./backup")
organize_files(folder_path)
rename_files_recursive(folder_path, "project")

print("Files backed up, organized, and renamed! ✅")
