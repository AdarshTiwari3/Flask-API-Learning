from numpy import * 
mat=matrix('1 2 3; 4 5 6; 7 8 9')

print("matrix=", mat)
print("diagonal elements of matrix=", mat.diagonal())
print("Diagonal elements of matrix=", diagonal(mat))
print("sum of diagonal elements of matrix=", mat.diagonal().sum())
# print("upper triangular elements of matrix=", mat.triu())
# print("lower triangular elements of matrix=", mat.tril())
print("transpose of matrix=", mat.T)
