def fibonacci(n):
    fibo=[0, 1]
    for i in range(2, n):
        fibo.append(fibo[i-1]+fibo[i-2])
    return fibo

n=int(input("Enter the number of elements in the fibonacci sequence: "))
x=fibonacci(n)
print("Fibonacci series: {}".format(x))

#using recursion    
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter the number of elements in the fibonacci sequence: "))
fibonacci(n)
print("{} index value in Fibonacci: {}".format(n,fibonacci(n)))