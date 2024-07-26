#operator overloading

class Student:
    def __init__(self, marks1, marks2):
        self.marks1=marks1
        self.marks2=marks2
    def __add__(self, other):
        m1=self.marks1+other.marks1
        m2=self.marks2+other.marks2
        stu=Student(m1, m2)
        return stu
    def __gt__(self, other):
        r1=self.marks1+self.marks2
        r2=other.marks1+other.marks2
        if r1>r2:
            return True
        else:
            return False
    def __str__(self):
        return "{} {}".format(self.marks1, self.marks2)
        # return self.marks1, self.marks2

stu1 = Student(10, 20)
stu2 = Student(30, 40)
stu4=Student("Ram", "Shyam")
stu5=Student("Hari", "Gopal")
stu6=stu4+stu5
stu3=stu1+stu2
print(stu3.marks1, stu3.marks2)
print("stu1>stu2=",stu1>stu2)
print(stu6.marks1, stu6.marks2)
# print(stu1.__str__()) #this will print the address of the object but after str method it will print the values of the object if we don't specify "{} {}".format then it will print the (val1, val2) in tuple format
print(stu1) #this will print the values of the object because of __str__ method