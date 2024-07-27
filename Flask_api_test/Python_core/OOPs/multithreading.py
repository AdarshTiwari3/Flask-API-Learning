#MultiThreading is a way to achieve multitasking. It is a process of executing multiple threads simultaneously.
from threading import *
from time import sleep
class Adarsh(Thread): #Inheriting Thread class and make Adars class as a thread
    def run (self):  #run is a method of Thread class so we are overriding it , otherwise it will give an error
        for i in range(100):
            print("Adarsh")
            sleep(1) #sleep is a method of time class that will sleep the program for 1 second

class Rohit(Thread): #Inheriting Thread class and make Rohit class as a thread
    def run (self):
        for i in range(100): #run is a method of Thread class so we are overriding it , otherwise it will give an error
            print("Rohit")
            sleep(1)
class Anoop(Thread): #Inheriting Thread class and make Anoop class as a thread
    def run(self):
        for i in range(100):
            print("Anoop")
            sleep(1)
adarsh=Adarsh()
rohit=Rohit()
anoop=Anoop()
# adarsh.run()  it won't work as we have to call start method of Thread class that will call run method internally
# rohit.run()   it won't work as we have to call start method of Thread class that will call run method internally
adarsh.start() #start method will call run method internally
rohit.start() #start method will call run method internally

anoop.start()