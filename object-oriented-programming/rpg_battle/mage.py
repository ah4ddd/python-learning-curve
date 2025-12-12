from character import Character
from random import randint

class Mage(Character):
    """Mage class - high attack, low defense, uses mana."""

    def __init__(self, name):
        """Initialize a mage with preset stats."""
        super().__init__(name, health=80, attack=40, defense=5)
        self.__mana = 100  # Private attribute
        self.__max_mana = 100

    @property
    def mana(self):
        """Get current mana."""
        return self.__mana

    @mana.setter
    def mana(self, value):
        """Set mana with validation."""
        if value < 0:
            self.__mana = 0
        elif value > self.__max_mana:
            self.__mana = self.__max_mana
        else:
            self.__mana = value

    def attack_target(self, target):
        """Mage's magical attack (polymorphism).

        Args:
            target (Character): Target to attack

        Returns:
            int: Damage dealt
        """
        mana_cost = 20

        if self.mana >= mana_cost:
            # Powerful spell
            self.mana -= mana_cost
            base_damage = self.attack + randint(5, 15)
            actual_damage = target.take_damage(base_damage)
            print(f"🔮 {self.name} (Mage) casts fireball on {target.name} for {actual_damage} damage! (Mana: {self.mana})")
        else:
            # Weak physical attack
            base_damage = 5 + randint(0, 3)
            actual_damage = target.take_damage(base_damage)
            print(f"💥 {self.name} (Mage) has no mana! Weak attack on {target.name} for {actual_damage} damage!")

        return actual_damage

    def restore_mana(self, amount=30):
        """Restore mana."""
        self.mana += amount
        print(f"{self.name} restored {amount} mana! (Mana: {self.mana})")

    def __str__(self):
        """Custom string representation."""
        base = super().__str__()
        return f"{base} | Mana: {self.mana}/{self.__max_mana}"
