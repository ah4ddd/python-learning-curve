from random import randint
from character import Character

class Rogue(Character):
    """Rogue class - balanced stats, can dodge and crit."""

    def __init__(self, name):
        """Initialize a rogue with preset stats."""
        super().__init__(name, health=100, attack=30, defense=10)
        self.dodge_chance = 0.25  # 25% dodge chance
        self.crit_chance = 0.30   # 30% crit chance

    def take_damage(self, damage):
        """Rogue can dodge attacks (method overriding).

        Args:
            damage (int): Incoming damage

        Returns:
            int: Actual damage taken (0 if dodged)
        """
        # Chance to dodge
        if randint(1, 100) <= self.dodge_chance * 100:
            print(f"💨 {self.name} (Rogue) dodged the attack!")
            return 0

        # Normal damage
        return super().take_damage(damage)

    def attack_target(self, target):
        """Rogue's attack with crit chance (polymorphism).

        Args:
            target (Character): Target to attack

        Returns:
            int: Damage dealt
        """
        base_damage = self.attack + randint(-5, 5)

        # Chance to crit
        if randint(1, 100) <= self.crit_chance * 100:
            base_damage *= 2
            actual_damage = target.take_damage(base_damage)
            print(f"🗡️ {self.name} (Rogue) CRITICAL HIT on {target.name} for {actual_damage} damage!")
        else:
            actual_damage = target.take_damage(base_damage)
            print(f"🗡️ {self.name} (Rogue) attacks {target.name} for {actual_damage} damage!")

        return actual_damage
