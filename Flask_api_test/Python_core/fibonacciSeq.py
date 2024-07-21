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
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
        
# n=int(input("Enter the number of elements in the fibonacci sequence: "))
if(n>0):
    fibonacci(n)
    print("{} index value in Fibonacci: {}".format(n,fibonacci(n)))

#using two variables
def fibonacci(n):
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
    fibonacci(n)