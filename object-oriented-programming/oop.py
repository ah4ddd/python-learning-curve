class Pizza:
    # CLASS VARIABLE:
    total_pizzas_made = 0

    def __init__(self, size, toppings):
        """INSTANCE METHOD (constructor)"""
        self.size = size
        self.toppings = toppings
        Pizza.total_pizzas_made += 1

    # ===== INSTANCE METHODS =====

    def bake(self):
        """
        INSTANCE METHOD: Works on THIS pizza
        - Needs self
        - Accesses self.size, self.toppings
        """
        print(f"🍕 Baking a {self.size} pizza with {', '.join(self.toppings)}...")

    def get_price(self):
        """
        INSTANCE METHOD: Calculate price of THIS pizza
        """
        base_price = {"small": 8, "medium": 10, "large": 12}
        price = base_price.get(self.size, 10)
        price += len(self.toppings) * 1.5
        return price

    # ===== CLASS METHODS =====

    @classmethod
    def margherita(cls, size):
        """
        CLASS METHOD: Alternative constructor for Margherita pizza
        - Needs cls to create object
        - Returns new Pizza object
        """
        return cls(size, ["cheese", "tomato", "basil"])

    @classmethod
    def pepperoni(cls, size):
        """CLASS METHOD: Alternative constructor for Pepperoni pizza"""
        return cls(size, ["cheese", "pepperoni"])

    @classmethod
    def get_total_pizzas(cls):
        """
        CLASS METHOD: Get class variable
        - Accesses cls.total_pizzas_made
        """
        return cls.total_pizzas_made

    # ===== STATIC METHODS =====

    @staticmethod
    def is_valid_size(size):
        """
        STATIC METHOD: Validate size
        - Doesn't need self or cls
        - Just checks if size is valid
        """
        return size in ["small", "medium", "large"]

    @staticmethod
    def calculate_delivery_fee(distance_km):
        """
        STATIC METHOD: Calculate delivery fee
        - Utility function
        - Doesn't need pizza data
        - Related to Pizza conceptually
        """
        if distance_km <= 5:
            return 2.0
        elif distance_km <= 10:
            return 4.0
        else:
            return 6.0

    def __str__(self):
        return f"{self.size.capitalize()} pizza with {', '.join(self.toppings)} - ₹{self.get_price():.2f}"

# ===== USING ALL THREE TYPES =====

print("=== STATIC METHODS (no object needed) ===")
print(f"Is 'large' valid? {Pizza.is_valid_size('large')}")
print(f"Is 'gigantic' valid? {Pizza.is_valid_size('gigantic')}")
print(f"Delivery fee for 7km: ₹{Pizza.calculate_delivery_fee(7)}")
print()

print("=== CLASS METHODS (create objects) ===")
pizza1 = Pizza.margherita("large")  # Using class method!
pizza2 = Pizza.pepperoni("medium")  # Using class method!
pizza3 = Pizza("small", ["cheese", "mushrooms", "olives"])  # Regular constructor
print()

print("=== INSTANCE METHODS (work on specific pizzas) ===")
pizza1.bake()
pizza2.bake()
pizza3.bake()
print()

print("=== DISPLAYING PIZZAS ===")
print(pizza1)
print(pizza2)
print(pizza3)
print()

print("=== CLASS METHOD (access class variable) ===")
print(f"Total pizzas made: {Pizza.get_total_pizzas()}")

# Output:
# === STATIC METHODS (no object needed) ===
# Is 'large' valid? True
# Is 'gigantic' valid? False
# Delivery fee for 7km: ₹4.0
#
# === CLASS METHODS (create objects) ===
#
# === INSTANCE METHODS (work on specific pizzas) ===
# 🍕 Baking a large pizza with cheese, tomato, basil...
# 🍕 Baking a medium pizza with cheese, pepperoni...
# 🍕 Baking a small pizza with cheese, mushrooms, olives...
#
# === DISPLAYING PIZZAS ===
# Large pizza with cheese, tomato, basil - ₹16.50
# Medium pizza with cheese, pepperoni - ₹13.00
# Small pizza with cheese, mushrooms, olives - ₹12.50
