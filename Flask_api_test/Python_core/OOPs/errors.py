#Type of error in python
# 1. Compile time error
# 2. Run time error
# 3. Logical error

num1=87
num2=0

try:
    res=num1/num2 #this is critical statement
    print("Result=",res)

except Exception as e: #This block will execute if any exception is raised
    print("Error:",e)
    print("Error occured, please check the input values.")

finally: #finally block will always execute whether the exception is raised or not
    print("Finally block executed.")