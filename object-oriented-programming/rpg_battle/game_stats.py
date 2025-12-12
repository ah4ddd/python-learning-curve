
# ==================== GAME STATISTICS ====================
from datetime import datetime
import json

class GameStats:
    """Track game statistics (class methods and properties)."""

    def __init__(self):
        """Initialize game stats."""
        self.__battles_fought = 0
        self.__victories = 0
        self.__defeats = 0
        self.__damage_dealt = 0
        self.__damage_taken = 0
        self.start_time = datetime.now()

    @property
    def battles_fought(self):
        return self.__battles_fought

    @property
    def victories(self):
        return self.__victories

    @property
    def win_rate(self):
        """Calculate win rate."""
        if self.__battles_fought == 0:
            return 0.0
        return (self.__victories / self.__battles_fought) * 100

    def record_battle(self, won, damage_dealt, damage_taken):
        """Record battle results.

        Args:
            won (bool): Whether player won
            damage_dealt (int): Total damage dealt
            damage_taken (int): Total damage taken
        """
        self.__battles_fought += 1
        if won:
            self.__victories += 1
        else:
            self.__defeats += 1

        self.__damage_dealt += damage_dealt
        self.__damage_taken += damage_taken

    def display_stats(self):
        """Display all statistics."""
        print("\n" + "="*50)
        print("GAME STATISTICS")
        print("="*50)
        print(f"Battles Fought: {self.__battles_fought}")
        print(f"Victories: {self.__victories}")
        print(f"Defeats: {self.__defeats}")
        print(f"Win Rate: {self.win_rate:.1f}%")
        print(f"Total Damage Dealt: {self.__damage_dealt}")
        print(f"Total Damage Taken: {self.__damage_taken}")

        # Calculate play time
        play_time = datetime.now() - self.start_time
        minutes = play_time.seconds // 60
        seconds = play_time.seconds % 60
        print(f"Play Time: {minutes}m {seconds}s")
        print("="*50 + "\n")

    def save_to_file(self, filename="game_stats.json"):
        """Save stats to JSON file.

        Args:
            filename (str): File to save to
        """
        data = {
            "battles_fought": self.__battles_fought,
            "victories": self.__victories,
            "defeats": self.__defeats,
            "damage_dealt": self.__damage_dealt,
            "damage_taken": self.__damage_taken,
            "play_time_seconds": (datetime.now() - self.start_time).seconds
        }

        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

        print(f"Stats saved to {filename}!")
