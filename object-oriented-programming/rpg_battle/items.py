
# ==================== INVENTORY SYSTEM (COMPOSITION) ====================

class Item:
    """Base item class."""

    def __init__(self, name, description):
        """Initialize an item.

        Args:
            name (str): Item name
            description (str): Item description
        """
        self.name = name
        self.description = description

    def use(self, character):
        """Use the item (to be overridden by subclasses).

        Args:
            character (Character): Character using the item
        """
        raise NotImplementedError("Subclass must implement use()")

    def __str__(self):
        return f"{self.name}: {self.description}"


class HealthPotion(Item):
    """Health potion item."""

    def __init__(self):
        super().__init__("Health Potion", "Restores 50 HP")
        self.heal_amount = 50

    def use(self, character):
        """Use health potion on character.

        Args:
            character (Character): Character to heal
        """
        character.heal(self.heal_amount)


class ManaPotion(Item):
    """Mana potion item (only works for mages)."""

    def __init__(self):
        super().__init__("Mana Potion", "Restores 50 Mana (Mages only)")
        self.mana_amount = 50

    def use(self, character):
        """Use mana potion on character.

        Args:
            character (Character): Character to restore mana
        """
        if isinstance(character, Mage): # type: ignore
            character.restore_mana(self.mana_amount)
        else:
            print(f"{character.name} can't use mana potions!")

class Inventory:
    """Inventory system using magic methods."""

    def __init__(self):
        """Initialize empty inventory."""
        self.__items = []

    def __len__(self):
        """Return number of items (magic method)."""
        return len(self.__items)

    def __getitem__(self, index):
        """Get item by index (magic method)."""
        return self.__items[index]

    def __iter__(self):
        """Make inventory iterable (magic method)."""
        return iter(self.__items)

    def __str__(self):
        """String representation of inventory."""
        if not self.__items:
            return "Inventory: Empty"

        items_str = ", ".join(item.name for item in self.__items)
        return f"Inventory ({len(self)} items): {items_str}"

    def add_item(self, item):
        """Add item to inventory.

        Args:
            item (Item): Item to add
        """
        self.__items.append(item)
        print(f"Added {item.name} to inventory!")

    def use_item(self, index, character):
        """Use an item from inventory.

        Args:
            index (int): Item index
            character (Character): Character using the item
        """
        if 0 <= index < len(self.__items):
            item = self.__items.pop(index)
            item.use(character)
        else:
            print("Invalid item index!")
