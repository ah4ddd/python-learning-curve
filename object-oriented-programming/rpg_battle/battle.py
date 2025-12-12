
# ==================== BATTLE SYSTEM ====================

class Battle:
    """Battle system managing combat between characters."""

    def __init__(self, player, enemy, stats):
        """Initialize a battle.

        Args:
            player (Character): Player character
            enemy (Character): Enemy character
            stats (GameStats): Game statistics tracker
        """
        self.player = player
        self.enemy = enemy
        self.stats = stats
        self.turn = 1
        self.player_damage_dealt = 0
        self.player_damage_taken = 0

    def __str__(self):
        """Battle status display."""
        return f"\n{'='*50}\nTURN {self.turn}\n{self.player}\n{self.enemy}\n{'='*50}"

    def player_turn(self):
        """Handle player's turn.

        Returns:
            bool: True if player wants to continue
        """
        print(f"\n--- {self.player.name}'s Turn ---")
        print("1. Attack")
        print("2. Use Item")
        print("3. View Stats")
        print("4. Flee")

        choice = input("Choose action: ").strip()

        if choice == "1":
            damage = self.player.attack_target(self.enemy)
            self.player_damage_dealt += damage
            return True

        elif choice == "2":
            if len(self.player.inventory) == 0:
                print("Inventory is empty!")
                return self.player_turn()  # Try again

            print(f"\n{self.player.inventory}")
            for i, item in enumerate(self.player.inventory):
                print(f"{i}. {item}")

            try:
                item_index = int(input("Select item (or -1 to cancel): "))
                if item_index == -1:
                    return self.player_turn()
                self.player.inventory.use_item(item_index, self.player)
            except (ValueError, IndexError):
                print("Invalid selection!")
                return self.player_turn()

            return True

        elif choice == "3":
            self.stats.display_stats()
            return self.player_turn()  # Don't consume turn

        elif choice == "4":
            print(f"{self.player.name} fled the battle!")
            return False

        else:
            print("Invalid choice!")
            return self.player_turn()

    def enemy_turn(self):
        """Handle enemy's turn."""
        print(f"\n--- {self.enemy.name}'s Turn ---")
        damage = self.enemy.attack_target(self.player)
        self.player_damage_taken += damage

    def start(self):
        """Start the battle loop.

        Returns:
            bool: True if player won
        """
        print(f"\n🔥 BATTLE START: {self.player.name} vs {self.enemy.name}! 🔥")

        while self.player.is_alive and self.enemy.is_alive:
            print(self)

            # Player turn
            if not self.player_turn():
                # Player fled
                self.stats.record_battle(False, self.player_damage_dealt, self.player_damage_taken)
                return False

            if not self.enemy.is_alive:
                break

            # Enemy turn
            self.enemy_turn()

            if not self.player.is_alive:
                break

            self.turn += 1

        # Battle over
        if self.player.is_alive:
            print(f"\n🎉 {self.player.name} WINS! 🎉")
            self.stats.record_battle(True, self.player_damage_dealt, self.player_damage_taken)
            return True
        else:
            print(f"\n💀 {self.player.name} was defeated... 💀")
            self.stats.record_battle(False, self.player_damage_dealt, self.player_damage_taken)
            return False
