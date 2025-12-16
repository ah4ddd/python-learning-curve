from pathlib import Path

base = Path("projects")
users = ["ahad", "mia", "zexo"]

for user in users:
    user_dir = base / user
    (user_dir / "logs").mkdir(parents=True, exist_ok=True)
    (user_dir / "data").mkdir(exist_ok=True)
    (user_dir / "config").mkdir(exist_ok=True)
    (user_dir / "output").mkdir(exist_ok=True)

