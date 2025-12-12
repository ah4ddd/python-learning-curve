"""
RPG Battle Game - Comprehensive OOP Project
Demonstrates all OOP concepts learned in Chapter 9
"""
from random import choice
from battle import Battle
from game_stats import GameStats
from items import HealthPotion, ManaPotion, Inventory
from rogue import Rogue
from mage import Mage
from warrior import Warrior
from character import Character

class Game:
    """Main game class orchestrating everything."""

    # Class constants
    ENEMY_TYPES = [Warrior, Mage, Rogue]
    ENEMY_NAMES = ["Goblin", "Orc", "Troll", "Skeleton", "Bandit", "Dark Wizard"]

    def __init__(self):
        """Initialize the game."""
        self.player = None
        self.stats = GameStats()
        print("="*50)
        print("WELCOME TO RPG BATTLE GAME!")
        print("="*50)

    def create_player(self):
        """Create player character."""
        print("\nCreate your character!")

        while True:
            name = input("Enter your name: ").strip()
            if Character.is_valid_name(name):
                break
            print("Invalid name! Must be 3-20 alphanumeric characters.")

        print("\nChoose your class:")
        print("1. Warrior (High HP, High Defense)")
        print("2. Mage (High Attack, Uses Mana)")
        print("3. Rogue (Balanced, Can Dodge & Crit)")

        while True:
            choice = input("Choose (1-3): ").strip()
            if choice == "1":
                self.player = Warrior(name)
                break
            elif choice == "2":
                self.player = Mage(name)
                break
            elif choice == "3":
                self.player = Rogue(name)
                break
            else:
                print("Invalid choice!")

        print(f"\n✅ Created: {self.player}")

        # Give starting items
        self.player.inventory.add_item(HealthPotion())
        self.player.inventory.add_item(HealthPotion())
        if isinstance(self.player, Mage):
            self.player.inventory.add_item(ManaPotion())

    def create_enemy(self):
        """Create random enemy.

        Returns:
            Character: Random enemy
        """
        enemy_class = choice(self.ENEMY_TYPES)
        enemy_name = choice(self.ENEMY_NAMES)
        enemy = enemy_class(enemy_name)
        return enemy

    def play(self):
        """Main game loop."""
        self.create_player()

        battle_count = 0

        while self.player.is_alive: # type: ignore
            battle_count += 1

            print(f"\n{'='*50}")
            print(f"BATTLE #{battle_count}")
            print(f"{'='*50}")

            # Heal player between battles
            if battle_count > 1:
                heal_amount = 30
                self.player.heal(heal_amount) # type: ignore

            # Create enemy
            enemy = self.create_enemy()

            # Start battle
            battle = Battle(self.player, enemy, self.stats)
            won = battle.start()

            if not won:
                break

            # Reward for winning
            print("\n🎁 Victory Rewards!")
            reward_item = choice([HealthPotion(), HealthPotion(), ManaPotion()])
            self.player.inventory.add_item(reward_item) # type: ignore

            # Continue?
            print(f"\n{self.player}")
            continue_choice = input("\nContinue to next battle? (y/n): ").strip().lower()
            if continue_choice != 'y':
                break

        # Game over
        print("\n" + "="*50)
        print("GAME OVER!")
        print("="*50)
        print(f"Total Characters Created: {Character.get_total_characters()}")
        self.stats.display_stats()

        # Save stats
        save = input("Save statistics? (y/n): ").strip().lower()
        if save == 'y':
            self.stats.save_to_file()


# ==================== RUN THE GAME ====================

if __name__ == "__main__":
    game = Game()
    game.play()
