import array

a = array.array('i',[1,2,3,4,5])
l = len(a)
print(l)
for i in range(0, l):
    print("ELEMENT ", i, " is ", a[i])

a = [1, 2, 3, 4, 5]

for i, value in enumerate(a):
    print(f"ELEMENT {i} is {value}")
