import array

a = array.array('i',[1,2,3,4,5])
l = len(a)
for i in range(0, l):
    print("ELEMENT ", i, " is ", a[i])
