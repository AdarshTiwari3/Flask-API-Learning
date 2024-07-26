#iterator is an object that contains a countable number of values.
#An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
#Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

lst=[1,2,3,4,5]
iterable=iter(lst)
print(next(iterable))
print(next(iterable))

print("<---------------Custom iterator--------------->")
#goes one by one till last element and it checks for the last element internally

#creating an iterator
class MyNumbers:
    def __init__(self):
        self.a=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.a<=100:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
        
myclass=MyNumbers()
print(next(myclass))
print("Using for loop")
for i in myclass:
    print(i)