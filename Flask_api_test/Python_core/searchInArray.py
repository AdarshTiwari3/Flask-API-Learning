from array import *
arr=array('i',[])
n=int(input("Enter the length of array: "))
for i in range(n):
    x=int(input("Enter the value: "))
    arr.append(x)

print(arr)

val=int(input("Enter the value to search: "))
for i in arr:
    if i==val:
        print("Value found at index: ",arr.index(i))
        break
else: print("Value not found")