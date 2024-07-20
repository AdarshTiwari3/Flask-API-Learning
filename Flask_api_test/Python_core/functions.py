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
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(swap_two_numbers(a, b))

# function to take variable length arguments
def sum(*varLen):
    s=0
    for i in varLen:
        s=s+i
    return s
print(sum(a, b, 3, 4, 5)) # takes as a tuple