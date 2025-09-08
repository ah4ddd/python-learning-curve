import os
import shutil

folder_path = "./my_folder"  # Change this to your folder

def organize_files(path):
    for filename in os.listdir(path):  # list all files/folders
        file_path = os.path.join(path, filename)  # get full path
        if os.path.isfile(file_path):  # check if it’s a file
            ext = filename.split('.')[-1]  # get file extension
            ext_folder = os.path.join(path, ext)  # folder for that type
            if not os.path.exists(ext_folder):
                os.makedirs(ext_folder)  # create folder if not exists
            shutil.move(file_path, os.path.join(ext_folder, filename))  # move file

def rename_files(path, prefix):
    for count, filename in enumerate(os.listdir(path), 1):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            ext = filename.split('.')[-1]
            new_name = f"{prefix}_{count}.{ext}"  # new name
            new_path = os.path.join(path, new_name)
            os.rename(file_path, new_path)  # rename

def backup_files(path, backup_folder):
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            shutil.copy(file_path, os.path.join(backup_folder, filename))

organize_files(folder_path)
rename_files(folder_path, "project")
backup_files(folder_path, "./backup")
print("Files organized, renamed, and backed up! ✅")
