import os
import shutil

def rename_files(path, prefix):
    files = os.listdir(path)
    for index, filename in enumerate(files):
        old_path = os.path.join(path, filename)
        if os.path.isfile(old_path):
            new_name = f"{prefix}_{index}{os.path.splitext(filename)[1]}"
            new_path = os.path.join(path, new_name)
            shutil.move(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")

