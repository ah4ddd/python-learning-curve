from contextlib import contextmanager

@contextmanager
def simple_context():
    print("🟢 SETUP: entering context")
    try:
        yield "RESOURCE"
    finally:
        print("🔴 CLEANUP: exiting context")

print("Before with")

with simple_context() as r:
    print("Inside with block")
    print("Using:", r)

print("After with")

