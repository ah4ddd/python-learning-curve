class Counter:
    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

for i in Counter(3):
    print(i)
