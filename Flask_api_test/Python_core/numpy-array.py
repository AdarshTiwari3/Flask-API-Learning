from numpy import *
arr=array([])
n=int(input("Enter the length of array: "))
for i in range(n):
    x=int(input("Enter the value: "))
    arr=append(arr,x)

print(arr)

val=int(input("Enter the value to search: "))
for i,value in enumerate(arr):
    if value==val:
        print("Value found at index: ",i,"Value: ",value)
        break
else: print("Value not found")