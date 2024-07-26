#method overloading
class Student:
    def __init__(self, marks1, marks2):
        self.marks1=marks1
        self.marks2=marks2

    def add(self, a=None, b=None, c=None): #as we can not write multiple methods with the same name in python so we can use default arguments to achieve method overloading
        if a and b and c:
            return a+b+c
        elif a and b:
            return a+b
        else:
            return a


stu1 = Student(10, 20)
print("sum=",stu1.add(10, 20, 30))
print("sum=",stu1.add(10, 20))
print("sum=",stu1.add(10))
print("sum=",stu1.add())
