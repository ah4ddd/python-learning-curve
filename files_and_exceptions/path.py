from pathlib import Path

structure = {
    "src": ["main.py", "utils.py"],
    "tests": ["test_main.py"],
    "docs": ["readme.md"]
}

base = Path("my_project")
base.mkdir()

for folder, files in structure.items():
    folder_path = base / folder
    folder_path.mkdir()
    for file in files:
        (folder_path / file).touch()
