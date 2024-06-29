from array import *
arr = array('i', [1, 2, 3, 4, 5])
for i in arr:
    print(i)
print()
newArray = array(arr.typecode, (a for a in arr)) #takes one-one value at a time from arr and stores it in newArray
for i in newArray:
    print(i)