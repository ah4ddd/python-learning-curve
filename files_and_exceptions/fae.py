from pathlib import Path

# Create a path object
file_path = Path("data.txt")
print(file_path)  # data.txt
print(type(file_path))  # <class 'pathlib.PosixPath'> or <class 'pathlib.WindowsPath'>
