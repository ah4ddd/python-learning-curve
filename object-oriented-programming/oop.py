class Capitalizer:
    def __call__(self, text):
        return text.upper()

cap = Capitalizer()
print(cap("hello"))

class Square:
    def __call__(self, x):
        f = x * x
        print(f)

s = Square()
s(5)
