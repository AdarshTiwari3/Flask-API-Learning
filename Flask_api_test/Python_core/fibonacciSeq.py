def fibonacci(n):
    fibo=[0, 1]
    for i in range(2, n):
        fibo.append(fibo[i-1]+fibo[i-2])
    return fibo

try:
    n = int(input("Enter the number of elements in the Fibonacci sequence: "))
    if n <= 0:
        raise ValueError("The number must be a positive integer.")
except ValueError as e:
    print(e)
if(n>0):
    x=fibonacci(n)
    print("Fibonacci series: {}".format(x))

#using recursion    
def fibonacci_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

# pos = int(input("Enter the position in the Fibonacci sequence: "))
if n >= 0:
    print("Fibonacci number at position {}: {}".format(n, fibonacci_rec(n-1)))
else:
    print("Please enter a non-negative integer.")

#using two variables
def fibonacci_two_variables(n):
    x=0
    y=1
    if(n==1):
        print(x)
    else:
        print(x, y, end=" ")
        for i in range(2,n):
            sum=x+y
            #now swap value of y with sum and x with y
            x=y
            y=sum
            print(sum, end=" ")

if(n>0):
    fibonacci_two_variables(n)