from numpy import * 
mat=matrix('1 2 3; 4 5 6; 7 8 9')

print("matrix=", mat)
print("diagonal elements of matrix=", mat.diagonal())
print("Diagonal elements of matrix=", diagonal(mat))
print("sum of diagonal elements of matrix=", mat.diagonal().sum())
print("min of matrix=", mat.min())
print("max of matrix=", mat.max())
print("transpose of matrix=", mat.T)
mat2=matrix('1 2 3; 7 5 6; 7 8 10')
mat3=mat+mat2
print("addition of matrix=", mat3)
print("subtraction of matrix=", mat-mat2)
print("multiplication of matrix=", mat*mat2)
print("division of matrix=", mat/mat2)
