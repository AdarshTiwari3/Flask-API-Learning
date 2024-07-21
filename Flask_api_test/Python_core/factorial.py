import sys
limit=sys.getrecursionlimit()
print("Recursion limit is: ", limit)

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
    print("Factorial of {} is: {}".format(n, facto))
else:
    print("Please enter a non-negative integer.")

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

#map filter reduce
#filter function
lst=[1,2,3,4,8,99,3,5,6,7,9,10]
x=filter(lambda x: x%2!=0, lst) #filter function takes two arguments, one is the function and the other is the iterable
print(list(x))

#map function
x=map(lambda x: x*x, lst) #map function takes two arguments, one is the function and the other is the iterable
print(list(x)) #map function returns a map object, so we need to convert it into list, [1, 4, 9, 16, 64, 9801, 9, 25, 36, 49, 81, 100]

#reduce function

x=reduce(lambda x, y: x+y, lst) #reduce function takes two arguments, one is the function and the other is the iterable
print(x) #reduce function returns a single value, 157
#working-
#1+2=3 x+y
#3+3=6 x+y, x gets total value and y gets list values one by one
#6+4=10
#10+8=18
#18+99=117
#117+3=120
#120+5=125
#125+6=131
#131+7=138
#138+9=147
#147+10=157