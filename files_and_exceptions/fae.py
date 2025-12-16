from pathlib import Path

def setup_project():
    """Create a professional project structure."""

    # Define structure
    base = Path("test_proj")

    folders = [
        base / "data" / "input",
        base / "data" / "output",
        base / "config",
        base / "logs",
        base / "scripts",
        base / "tests"
    ] #path objects

    # Create all folders
    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)
        print(f"✅ Created: {folder}")

    # Create some default files
    (base / "README.md").write_text("# My Project\n\nProject description here.")
    (base / "config" / "settings.txt").write_text("# Settings\nversion=1.0\n")
    (base / ".gitignore").write_text("__pycache__/\n*.pyc\nlogs/\n")

    print("\n✅ Project structure created!")

    # Display the structure
    print("\n📁 Project Structure:")
    display_tree(base)

def display_tree(directory, prefix=""):
    """Display directory tree."""
    items = sorted(directory.iterdir(), key=lambda x: (not x.is_dir(), x.name))

    for i, item in enumerate(items):
        is_last = i == len(items) - 1
        current_prefix = "└── " if is_last else "├── "
        print(f"{prefix}{current_prefix}{item.name}")

        if item.is_dir():
            next_prefix = prefix + ("    " if is_last else "│   ")
            display_tree(item, next_prefix)

setup_project()
