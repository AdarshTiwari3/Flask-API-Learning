class Name:
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

instance1=Name("Adarsh")
print(instance1.getName())
instance1.setName("Adarsh Tiwari")
print(instance1.getName())

class Contact:
    isHuman=True             #class variable , this goes in the class namespace
    def __init__(self, name, phoneNumber):
        self.name=name  #instance variable, this goes in the instance namespace
        self.phoneNumber=phoneNumber #instance variable
    
    def getContact(self): #getter method or accessor method, instance method because it is using instance variables
        print("Name:{} and Contact Number:{}".format(self.name, self.phoneNumber))

    def setContact(self, name, phoneNumber): #setter method or mutator method, instance method
        self.name=name
        if(phoneNumber.isdigit() and len(phoneNumber)==10):
            self.phoneNumber=phoneNumber
        else:
            print("Incorrect Phone Number Format, Please enter a valid phone number.")
            self.phoneNumber=None
    @classmethod
    def isHumancheck(cls): #class method because it is using class variable
        print("Human:{}".format(cls.isHuman))
    @staticmethod
    def info():
        print("This is a static method.") #static method because it is not using any instance or class variables

contact1=Contact("Adarsh", '9293293292')
contact1.getContact()
contact1.setContact("Rohit Tiwari", '7293293292')
contact1.getContact()
contact1.setContact("Rohit Tiwari", '7293293200')
contact1.getContact()
print(contact1.isHuman)
Contact.isHuman=False #changing the class variable
print(contact1.isHuman)
Contact.isHumancheck()
Contact.info()