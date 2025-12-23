from contextlib import contextmanager

@contextmanager
def demo():
    print("A: setup starts")
    try:
        print("B: before yield")
        yield "RESOURCE"
        print("E: after yield (normal exit)")
    finally:
        print("F: cleanup runs")

print("0: before with")

with demo() as r:
    print("C: inside with")
    print("D: r =", r)

print("G: after with")
