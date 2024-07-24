#inheritance
class A:
    def feature1(self):
        print("I am Feature 1")
    def feature2(self):
        print("I am Feature 2")
class B(A): # B is inheriting class A
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
    def feature6(self):
        print("I am Feature 6")
class E(A, D): # E is inheriting class A and D, this is an example of multiple inheritance
    def feature7(self):
        print("I am Feature 7")
    def feature8(self):
        print("I am Feature 8")

b1=B()
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

