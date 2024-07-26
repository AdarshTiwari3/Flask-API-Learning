#method overriding is the concept of OOPs in which a method of the parent class is redefined in the child class with the same name and signature.

class A:
    def display(self):
        print("I am class A")

class B(A):
    
    def display(self): # this is the method overriding, this will override the display
        # super().display() # this will call the display method of class A
        print("I am class B")

b1=B()
b1.display() # this will call the display method of class B because it is present in class B, if it is not present in class B then it will call the display method of class A