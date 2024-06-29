from numpy import *
arr=array([1,2,3,4,5],int)
print("array=",arr)

# linspace() way to create an array
arrr=linspace(0,15,16) # 0 to 15 with 16 elements/parts
print("linspace() way to create an array=",arrr)
arrr=linspace(0,15) # 0 to 15 with default 50 elements/parts
print("linspace() way to create an array=",arrr)

# arange() way to create an array
arrr=arange(0,15,2) # 0 to 15 with 2 steps
print("arange() way to create an array=",arrr)
arrr=arange(0,15) # 0 to 15 with default 1 step
print("arange() way to create an array=",arrr)

# logspace() way to create an array
arrr=logspace(0,15,16) # 0 to 15 with 16 elements/parts in log scale from 10^0 to 10^15
print("logspace() way to create an array=",arrr)

# zeros() way to create an array
arrr=zeros(5,int) # 5 zeros
print("zeros() way to create an array=",arrr)

# ones() way to create an array
arrr=ones(5,int) # 5 ones
print("ones() way to create an array=",arrr)