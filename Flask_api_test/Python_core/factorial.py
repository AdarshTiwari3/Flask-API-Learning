def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        fact=1
        for i in range(1, n+1):
            fact=fact*i
        return fact




n=int(input("Enter the factorial number: "))
facto=factorial(n)
print("Factorial of {} is: {}".format(n, facto))

#using recursion
def factorial_recursion(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

fact=factorial_recursion(n)
print("Factorial of {} using recursion is: {}".format(n, fact))

