# ==================== CHILD CLASSES (INHERITANCE) ====================
from random import randint
from character import Character

class Warrior(Character):
    """Warrior class - high health and defense."""

    def __init__(self, name):
        """Initialize a warrior with preset stats."""
        super().__init__(name, health=150, attack=25, defense=20)
        self.rage = 0  # Warrior-specific attribute

    def attack_target(self, target):
        """Warrior's powerful attack (method overriding - polymorphism).

        Args:
            target (Character): Target to attack

        Returns:
            int: Damage dealt
        """
        # Warrior builds rage and deals extra damage
        self.rage += 10
        bonus_damage = self.rage // 20

        base_damage = self.attack + bonus_damage + randint(-3, 8)
        actual_damage = target.take_damage(base_damage)

        print(f"⚔️ {self.name} (Warrior) strikes {target.name} for {actual_damage} damage! (Rage: {self.rage})")
        return actual_damage

    def __str__(self):
        """Custom string representation."""
        base = super().__str__()
        return f"{base} | Rage: {self.rage}"
