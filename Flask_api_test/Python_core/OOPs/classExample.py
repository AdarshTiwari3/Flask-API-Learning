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
    def __init__(self, name, phoneNumber):
        self.name=name
        self.phoneNumber=phoneNumber
    
    def getContact(self):
        print("Name:{} and Contact Number:{}".format(self.name, self.phoneNumber))

    def setContact(self, name, phoneNumber):
        self.name=name
        if(phoneNumber.isdigit() and len(phoneNumber)==10):
            self.phoneNumber=phoneNumber
        else:
            print("Incorrect Phone Number Format, Please enter a valid phone number.")
            self.phoneNumber=None

contact1=Contact("Adarsh", '9293293292')
contact1.getContact()
contact1.setContact("Rohit Tiwari", '7293293292')
contact1.getContact()
contact1.setContact("Rohit Tiwari", '7293293200')
contact1.getContact()