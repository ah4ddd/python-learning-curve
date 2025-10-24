name = "Global Alice"

def outer_function():
    name = "Outer Bob"

    def inner_function():
        name = "Inner Charlie"
        print(f"Inner: {name}")

    inner_function()
    print(f"Outer: {name}")

outer_function()
print(f"Global: {name}")
