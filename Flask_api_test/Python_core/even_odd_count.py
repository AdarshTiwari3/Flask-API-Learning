def even_odd_count(lst):
    evenCount=0
    oddCount=0
    for i in lst:
        if i%2==0:
            evenCount+=1
        else:
            oddCount+=1
    return evenCount, oddCount

lst=[]
n=int(input("Enter number of elements to be inserted in the list: "))
for i in range(n):
    x=int(input("Enter element:"))
    lst.append(x)
print("List=", lst)
even, odd=even_odd_count(lst)
print("Even:{}, Odd:{}".format(even, odd))