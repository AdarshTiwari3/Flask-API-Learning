class Student:
    def __init__(self, name, rollNumber, city, state):
        self.name = name
        self.rollNumber = rollNumber
        self.address = self.Address(city, state)
    
    def getStudent(self):
        print("Name: {}\nRoll Number: {}".format(self.name, self.rollNumber))
        self.address.getAddress()
        
    def setStudent(self, name, rollNumber):
        self.name = name
        self.rollNumber = rollNumber

    class Address:
        def __init__(self, city, state):
            self.city = city
            self.state = state
        
        def getAddress(self):
            print("City: {}\nState: {}".format(self.city, self.state))
        
        def setAddress(self, city, state):
            self.city = city
            self.state = state

# Create an instance of the Student class
stu1 = Student("Adarsh", 1, "New Delhi", "Delhi")
stu1.getStudent()
stu1.setStudent("Ronny Tiwari", 2)
stu1.getStudent()
# Update the address of the student
addr1=stu1.Address("Noida", "Uttar Pradesh")
addr1.getAddress()
stu1.address.setAddress("Ghaziabad", "Uttar Pradesh") #because it is linked to the stu1 instance of the Student class
stu1.getStudent()
stu1.address.getAddress()
