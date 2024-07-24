#inheritance
class A:
    def __init__(self):
        print("I am inside class A constructor")

    def feature1(self):
        print("I am Feature 1")
    def feature2(self):
        print("I am Feature 2")
class B(A): # B is inheriting class A
    def __init__(self):
        super().__init__() # this will call the constructor of the parent class
        print("I am inside class B constructor")
    def feature3(self):
        print("I am Feature 3")
    def feature4(self):
        print("I am Feature 4")

class C(B): # C is inheriting class B,his is an example of multilevel inheritance
    def display(self):
        print("I am in Class C")

class D:
    def feature5(self):
        print("I am Feature 5")
    def feature2(self):
        print("I am Feature 2-D")
class E(A, D): # E is inheriting class A and D, this is an example of multiple inheritance
    def __init__(self):
        super().__init__() # this will call the constructor of the parent class, MRO(Method Resolution Order) is used to resolve the conflicts in multiple inheritance, it goes from left to right
        print("I am inside class E constructor")
    def feature7(self):
        print("I am Feature 7")
    def feature8(self):
        print("I am Feature 8")

b1=B() # this will call the constructor of class B if it is present, if not then it will call the constructor of class A otherwise it will call the constructor of the parent class, we can also call the constructor of the parent class using super
b1.feature1()
b1.feature2()
b1.feature3()
c1=C()
c1.display()
c1.feature1()
c1.feature3()
e1=E()
e1.feature1()
e1.feature5()
e1.feature7()
e1.feature2() # this will call the feature2 of class A because it is present in class A, If it is not present in class A then it will call the feature2 of class D (MRO)

