from pathlib import Path

# Create some test files first
test_dir = Path("test_files")
test_dir.mkdir(exist_ok=True)

# Create some files
(test_dir / "file1.txt").write_text("Content 1")
(test_dir / "file2.txt").write_text("Content 2")
(test_dir / "data.json").write_text('{"key": "value"}')
(test_dir / "readme.md").write_text("# Readme")

# List all items
print("All items:")
for item in test_dir.iterdir():
    print(f"  {item.name}")

# List only .txt files
print("\nOnly .txt files:")
for item in test_dir.glob("*.txt"):
    print(f"  {item.name}")

# List all files recursively (including subfolders)
print("\nAll files recursively:")
for item in test_dir.rglob("*"):
    if item.is_file():
        print(f"  {item}")
