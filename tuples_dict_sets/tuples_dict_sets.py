F = "f","s","o","c","i","e","t","y"

print(F)

lst = [1,2,3]
t = tuple(lst)
print(t)

z = 1; n =4; j = 8;
packed = z, n, j

print (packed)

x, c, v = (34, 35, 36)

print (x, c, v)

tupe = ("fun", "not", "for", "me", "not")

tupe[0]

for t in range (len(tupe)):
    print(tupe[t])

not_count = tupe.count("not")

print (not_count)

indx = tupe.index("me")
print(indx)

person = ("Ahad", 22, "India")
name, age, country = person

print (person)

head, *middle, tail = (1,2,3,4,5)
print (head)

matrix = ((1,2,3), (4,5,6), (7,8,9))
print (matrix[2][2])

print(max(matrix))
print(min(matrix))

def stats(nums):
    s = sum(nums)
    n = len(nums)
    mean = s / n
    print(mean)
    return s, n, mean

total, count, average = stats([10,20,30])

coord = (28.6139, 77.2090)
lat, lon = coord

print("Latitude:", lat)
print("Longitude:", lon)

visits = {}
location = (51.5074, -0.1278)
visits[location] = "London"

print (visits)

colors = ("red", "green", "white")
print(colors[1])

def min_max(nums):
    print(max(nums))
    print(min(nums))

min_max((12, 30, 40, 50, 900))

HOME = (3,6)
BIKE = (2,4)
BAR = (5,10)

coordinates = [HOME, BIKE, BAR]

map = {
    HOME: "HOME",
    BIKE: "BIKE",
    BAR: "BAR"
}

data = (1,2,3,4,5)
print (data)
z, *b, f = data
print((f,*b,z))
