class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @radius.deleter
    def radius(self):
        """This method is called when someone does: del circle.radius"""
        print("Deleter called - resetting radius")
        self._radius = 0

# Usage
circle = Circle(5)
print(circle.radius)
del circle.radius  # Calls the deleter method
print(circle.radius)  # Now returns 0
