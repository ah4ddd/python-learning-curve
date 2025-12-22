class DemoContext:
    def __enter__(self):
        print("🟢 ENTER: setup happens")
        return "RESOURCE"

    def __exit__(self, exc_type, exc_value, traceback):
        print("🔴 EXIT: cleanup happens")
        print(f"   exc_type = {exc_type}")
        print(f"   exc_value = {exc_value}")
        print("   resource released")

with DemoContext() as d:
    print("using",d)
