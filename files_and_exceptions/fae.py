from pathlib import Path
from random import choice
from datetime import datetime

class QuoteManager:
    """Manage Mia's quotes with proper file structure."""

    def __init__(self, base_dir="mia_quotes"):
        """Initialize with a base directory."""
        self.base_dir = Path(base_dir)
        self.quotes_file = self.base_dir / "quotes.txt"
        self.log_file = self.base_dir / "logs" / "access.log"

        # Create directory structure
        self.setup_directories()

    def setup_directories(self):
        """Create necessary directories."""
        # Create base directory
        self.base_dir.mkdir(exist_ok=True)

        # Create logs subdirectory
        (self.base_dir / "logs").mkdir(exist_ok=True)

        print(f"✅ Directories ready: {self.base_dir}")

    def add_quote(self, quote):
        """Add a new Mia quote."""
        with open(self.quotes_file, "a") as f:
            f.write(quote + "\n")
        print(f"✅ Quote added: '{quote}'")
        self.log_action(f"Added quote: {quote}")

    def get_random_quote(self):
        """Get a random quote."""
        if not self.quotes_file.exists():
            return "No quotes yet! Add some first."

        with open(self.quotes_file, "r") as f:
            quotes = [line.strip() for line in f if line.strip()]

        if not quotes:
            return "No quotes yet!"

        quote = choice(quotes)
        self.log_action(f"Retrieved quote: {quote}")
        return quote

    def list_all_quotes(self):
        """List all quotes."""
        if not self.quotes_file.exists():
            print("No quotes file found!")
            return

        with open(self.quotes_file, "r") as f:
            quotes = [line.strip() for line in f if line.strip()]

        print(f"\n💬 MIA'S QUOTES ({len(quotes)} total):")
        print("="*50)
        for i, quote in enumerate(quotes, 1):
            print(f"{i}. {quote}")

        self.log_action("Listed all quotes")

    def log_action(self, action):
        """Log an action with timestamp."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {action}\n"

        with open(self.log_file, "a") as f:
            f.write(log_entry)

    def show_logs(self):
        """Display all logs."""
        if not self.log_file.exists():
            print("No logs yet!")
            return

        print("\n📋 ACCESS LOGS:")
        print("="*50)
        with open(self.log_file, "r") as f:
            print(f.read())

    def get_stats(self):
        """Display statistics."""
        quote_count = 0
        if self.quotes_file.exists():
            with open(self.quotes_file, "r") as f:
                quote_count = len([line for line in f if line.strip()])

        log_count = 0
        if self.log_file.exists():
            with open(self.log_file, "r") as f:
                log_count = len(f.readlines())

        print(f"\n📊 STATISTICS:")
        print(f"  Total quotes: {quote_count}")
        print(f"  Total log entries: {log_count}")
        print(f"  Quotes file: {self.quotes_file}")
        print(f"  Log file: {self.log_file}")

# Use it!
manager = QuoteManager()

# Add some of Mia's finest roasts
manager.add_quote("Why are you still coding? It's 2 AM!")
manager.add_quote("Your variable names are atrocious.")
manager.add_quote("Did you even test that?")
manager.add_quote("I'm not impressed. Do better.")

# Get random quote
print(f"\n💬 Random Mia quote: '{manager.get_random_quote()}'")

# List all
manager.list_all_quotes()

# Show stats
manager.get_stats()

# Show logs
manager.show_logs()
