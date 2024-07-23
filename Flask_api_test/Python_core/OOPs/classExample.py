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