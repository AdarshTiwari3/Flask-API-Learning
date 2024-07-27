#MultiThreading is a way to achieve multitasking. It is a process of executing multiple threads simultaneously.
from threading import *
from time import sleep
class Adarsh(Thread): #Inheriting Thread class and make Adars class as a thread
    def run (self):  #run is a method of Thread class so we are overriding it , otherwise it will give an error
        for i in range(10):
            print("Adarsh")
            sleep(1) #sleep is a method of time class that will sleep the program for 1 second

class Rohit(Thread): #Inheriting Thread class and make Rohit class as a thread
    def run (self):
        for i in range(10): #run is a method of Thread class so we are overriding it , otherwise it will give an error
            print("Rohit")
            sleep(1)
class Anoop(Thread): #Inheriting Thread class and make Anoop class as a thread
    def run(self):
        for i in range(10):
            print("Anoop")
            sleep(1)
adarsh=Adarsh()
rohit=Rohit()
anoop=Anoop()
# adarsh.run()  it won't work as we have to call start method of Thread class that will call run method internally
# rohit.run()   it won't work as we have to call start method of Thread class that will call run method internally
adarsh.start() #start method will call run method internally
sleep(0.2) #sleeping for 0.2 seconds to avoid collision between threads
rohit.start() #start method will call run method internally
sleep(0.2) #sleeping for 0.2 seconds to avoid collision between threads
anoop.start()
adarsh.join() #join method will wait for the thread to complete its execution
rohit.join() #join method will wait for the thread to complete its execution
anoop.join() #join method will wait for the thread to complete its execution
print("Bye") #this will be printed after the completion of all the threads , main thread handles this
#In big application we don't use sleep method as there each thread will have its own time to execute here its too small so we are using sleep method