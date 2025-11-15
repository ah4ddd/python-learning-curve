from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisines):
        super().__init__(name, cuisines)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'mint', 'cookie dough']

    def display_flavors(self):
        print(f"{self.name.title()} offers the following ice cream flavors:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")
