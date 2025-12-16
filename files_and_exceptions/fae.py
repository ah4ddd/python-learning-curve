from pathlib import Path

file_path = Path("data") / "projects" / "report.txt"

print(f"Full path: {file_path}")
print(f"Name: {file_path.name}")           # Filename
print(f"Stem: {file_path.stem}")           # Filename without extension
print(f"Suffix: {file_path.suffix}")       # Extension
print(f"Parent: {file_path.parent}")       # Parent directory
print(f"Parents: {list(file_path.parents)}")  # All parents
