def swap_two_numbers(a, b):
    a=a+b
    b=a-b
    a=a-b
    return a, b

print(swap_two_numbers(1, 2))
# using ^ operator
def swap_two_numbers(a, b):
    a=a^b # a=1^2=3
    b=a^b # b=3^2=1
    a=a^b  # a=3^1=2
    return a, b
print(swap_two_numbers(1, 2))

def swap_two_numbers(a, b):
    a, b=b, a
    return a, b
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
print(swap_two_numbers(5, 6))

# function to take variable length arguments
def sum(*varLen):
    s=0
    for i in varLen:
        s=s+i
    return s
print(sum(9, 6, 3, 4, 5)) # takes as a tuple

# function to take keyword variable length keyword arguments

def display(name, **varLen):
    print("name=", name)
    for key, value in varLen.items():
        print(key, value)

# display(name="Adarsh", age=20, city="New Delhi", country="India") # takes as a dictionary
display( age=20, city="New Delhi", country="India", name="Adarsh") #both are same

#global and local variables

globalVar=11
print("id-global=",id(globalVar))
def func():
    localVar=12
    globals()['globalVar'] # to change the value of global variable inside the function scope use globals() method
    # globalVar=13
    print("id-local=",id(localVar))
    
    # global globalVar
    print("id-global=",id(globalVar))
    
    print("localVar=", localVar)
    print("globalVar=", globalVar)

func()
print("globalVar=", globalVar)