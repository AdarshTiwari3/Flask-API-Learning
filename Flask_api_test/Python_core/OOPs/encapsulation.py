#encapsulation: Encapsulation is the process of restricting access to methods and variables in a class in order to prevent direct modification of data.
#Encapsulation is a way to achieve data hiding in OOPs.
#public, private, protected
#public: accessible from anywhere
#private: accessible only within the class
#protected: accessible within the class and its subclasses, although in python it doesn't force the access restriction
#Public Example:

class Name:
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
name=Name("Adarsh")
print(name.getName())
name.setName("Adarsh Tiwari")
print(name.getName())


#Private Example:
#in python, private variables are defined by using double underscore __ before the variable name
class Contact:
    __isHuman=True             #private class variable , this goes in the class namespace
    def __init__(self, name, phoneNumber):
        self.__name=name  #private instance variable, this goes in the instance namespace
        self.__phoneNumber=phoneNumber #private instance variable
    
    def getContact(self): #getter method or accessor method, instance method because it is using instance variables
        print("Name:{} and Contact Number:{}".format(self.__name, self.__phoneNumber))
    
    def setContact(self, name, phoneNumber): #setter method or mutator method, instance method
        self.__name=name
        if(phoneNumber.isdigit() and len(phoneNumber)==10):
            self.__phoneNumber=phoneNumber
        else:
            print("Incorrect Phone Number Format, Please enter a valid phone number.")
            self.__phoneNumber=None
    @classmethod
    def isHumancheck(cls): #class method because it is using class variable
        print("Human:{}".format(cls.__isHuman))
    @staticmethod
    def info():
        print("This is a static method.") #static method because it is not using any instance or class variables

contact=Contact("Adarsh", '9293293292')
contact.getContact()
# contact.__name() this will give an error because __name is a private variable
contact.setContact("Rohit Tiwari", '7293293292')
contact.getContact()

#Protected Example:
#in python, protected variables are defined by using single underscore _ before the variable name
class Address:
    _city="Noida"
    _state="Uttar Pradesh"
    def __init__(self, city, state):
        self._city=city
        self._state=state
    def getAddress(self):
        print("City: {}\nState: {}".format(self._city, self._state))
    def setAddress(self, city, state):
        self._city=city
        self._state=state
class HomeNumber(Address):
    def __init__(self, HomeNumber, city="Noida", state="Uttar Pradesh"):
        super().__init__(city, state)
        self.HomeNumber=HomeNumber
    def getHomeNumber(self):
        print("Home Number: {}".format(self.HomeNumber))
        print("City: {}\nState: {}".format(self._city, self._state))
addr=Address("Delhi", "Delhi")
addr.getAddress()
print("Protected-Variables",addr._city) #this will not give an error because _city is a protected variable because in python it doesn't force the access restriction
addr2=HomeNumber("123")
addr2.getHomeNumber()
