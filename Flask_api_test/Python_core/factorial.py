def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        fact=1
        for i in range(1, n+1):
            fact=fact*i
        return fact
#time complexity of this function is O(n)



n=int(input("Enter the factorial number: "))
if(n>0):
    facto=factorial(n)
else:
    print("Please enter a non-negative integer.")
print("Factorial of {} is: {}".format(n, facto))

#using recursion
def factorial_recursion(n):
    #time complexity of recursion is O(n)
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

if(n>0):
    fact=factorial_recursion(n)
    print("Factorial of {} using recursion is: {}".format(n, fact))
else:
    print("Please enter a non-negative integer.")

#using lambda function
fact=lambda n: 1 if n==0 or n==1 else n*fact(n-1)
#time complexity of lambda function is O(n)
if(n>0):
    print("Factorial of {} using lambda function is: {}".format(n, fact(n)))
else:
    print("Please enter a non-negative integer.")


#using reduce function
from functools import reduce
fact=reduce(lambda x, y: x*y, range(1, n+1)) #reduce function takes two arguments, one is the function and the other is the iterable
#time complexity of reduce function is O(n)
if(n>0):
    print("Factorial of {} using reduce function is: {}".format(n, fact))
else:
    print("Please enter a non-negative integer.")
