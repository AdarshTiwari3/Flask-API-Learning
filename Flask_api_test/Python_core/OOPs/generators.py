#generators are used to create iterators, but with a different approach. Generators are simple functions which return an iterable set of items, one at a time, in a special way.

def my_numbers():
    a=1
    while a<=100:
        yield a  #yield is used to return the value and it will not terminate the function, it will return the value and function will be in the same state
        a+=1

values=my_numbers()
print(next(values))

for i in values:
    print(i)

#Benefit-iterators loads every thing in memory, but generators don't load everything in memory, it loads one by one