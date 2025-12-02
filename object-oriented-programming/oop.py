import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self  # available as the variable after "as"

    def __exit__(self, *args):
        self.end = time.time()
        print("Time taken:", self.end - self.start)


with Timer() as t:
    for i in range(10_000_000):
        pass
