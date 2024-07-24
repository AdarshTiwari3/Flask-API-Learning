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

class C(B): # C is inheriting class B
    def display(self):
        print("I am in Class C")

#this is an example of multilevel inheritance
b1=B()
b1.feature1()
b1.feature2()
b1.feature3()
c1=C()
c1.display()
c1.feature1()
c1.feature3()

