# ==================== BASE CLASSES ====================
from random import randint
from items import Inventory

class Character:
    """Base character class (demonstrates inheritance).

    All character types inherit from this class.
    """

    # Class variable (shared by all characters)
    total_characters = 0

    def __init__(self, name, health, attack, defense):
        """Initialize a character.

        Args:
            name (str): Character's name
            health (int): Starting health points
            attack (int): Attack power
            defense (int): Defense rating
        """
        self.name = name
        self.__max_health = health  # Private attribute
        self.__health = health      # Private attribute
        self.attack = attack
        self.defense = defense
        self.is_alive = True
        self.inventory = Inventory()  # Composition

        Character.total_characters += 1

    # Property for encapsulation
    @property
    def health(self):
        """Get current health."""
        return self.__health

    @health.setter
    def health(self, value):
        """Set health with validation."""
        if value < 0:
            self.__health = 0
            self.is_alive = False
        elif value > self.__max_health:
            self.__health = self.__max_health
        else:
            self.__health = value

    @property
    def max_health(self):
        """Get max health (read-only)."""
        return self.__max_health

    # Magic methods
    def __str__(self):
        """String representation for users."""
        status = "Alive" if self.is_alive else "Dead"
        return f"{self.name} ({status}) - HP: {self.health}/{self.max_health}"

    def __repr__(self):
        """String representation for developers."""
        return f"Character('{self.name}', {self.health}, {self.attack}, {self.defense})"

    def __lt__(self, other):
        """Compare characters by health (for sorting)."""
        return self.health < other.health

    # Instance methods
    def take_damage(self, damage):
        """Take damage with defense calculation.

        Args:
            damage (int): Incoming damage

        Returns:
            int: Actual damage taken after defense
        """
        # Defense reduces damage
        actual_damage = max(1, damage - self.defense // 2)
        self.health -= actual_damage

        if self.health <= 0:
            self.is_alive = False

        return actual_damage

    def heal(self, amount):
        """Heal character.

        Args:
            amount (int): Amount to heal
        """
        if self.is_alive:
            self.health += amount
            print(f"{self.name} healed {amount} HP!")

    def attack_target(self, target):
        """Attack another character (polymorphism - overridden in subclasses).

        Args:
            target (Character): Target to attack

        Returns:
            int: Damage dealt
        """
        base_damage = self.attack + randint(-5, 5)
        actual_damage = target.take_damage(base_damage)
        print(f"{self.name} attacks {target.name} for {actual_damage} damage!")
        return actual_damage

    # Class method
    @classmethod
    def get_total_characters(cls):
        """Get total number of characters created.

        Returns:
            int: Total characters
        """
        return cls.total_characters

    # Static method
    @staticmethod
    def is_valid_name(name):
        """Validate character name.

        Args:
            name (str): Name to validate

        Returns:
            bool: True if valid
        """
        return len(name) >= 3 and len(name) <= 20 and name.isalnum()
