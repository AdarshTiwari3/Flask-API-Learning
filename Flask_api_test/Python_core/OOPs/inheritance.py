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
b1=B()
b1.feature1()
b1.feature2()
b1.feature3()