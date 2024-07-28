#linear search

def linear_search(arr, element):
    for i in arr:
        if i==element:
            print("i:",i)
            return arr.index(i)
            
    
    return "Element not found"
lst=[]
n=int(input("Enter the number of elements in the list: "))

for i in range(n):
    x=int(input("Enter {} element: ".format(i+1)))
    lst.append(x)

ele=int(input("Enter the element to be searched: "))

searchedElement=linear_search(lst, ele)

print("Element found at position: ", searchedElement)
