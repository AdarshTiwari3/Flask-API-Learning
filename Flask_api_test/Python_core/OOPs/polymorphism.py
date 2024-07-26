#Polymorphism: Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types). use one in many forms
#There are four ways to implement polymorphism:
#1. Duck Typing
#2. Operator Overloading
#3. Method Overloading
#4. Method Overriding

#Duck Typing: It is a concept related to dynamic typing, where the type or the class of an object is less important than the methods it defines. 
#it doesn't matter what type of object it is, it matters what methods it has

class VsCode:
    def display(self):
        print("I am inside VsCode")
        print("Program is executing...")

class Laptop:
    def code(self, editor):
        editor.display()

class MyEditor:
    def display(self):
        print("I am inside MyEditor")
        print("Program is executing...")

# editor=VsCode()
editor=MyEditor()
lap=Laptop()
# lap.code(editor)
lap.code(editor)

a=10
b=23
c=int.__add__(a,b)
print("c=", c)