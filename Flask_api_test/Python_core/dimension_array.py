from numpy import * 
arr=array(
    [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ], int
)
print("array=", arr)
print("dimension of array=", arr.ndim)
print("shape of array=", arr.shape)
print("size of array=", arr.size)
print("type of array=", arr.dtype)
print("itemsize of array=", arr.itemsize) # size of each element in bytes
print("nbytes of array=", arr.nbytes) # total size of array in bytes    8x9=72
