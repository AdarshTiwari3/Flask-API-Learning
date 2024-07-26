#method overriding is the concept of OOPs in which a method of the parent class is redefined in the child class with the same name and signature.

class A:
    def display(self):
        print("I am class A")

class B(A):
    pass

b1=B()
b1.display() # this will call the display method of class A because it is not present in class B