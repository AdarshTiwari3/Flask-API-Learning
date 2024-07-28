#binary search



def binary_search(arr, element):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high-1)//2
        if arr[mid]==element:
            # print("Element found at position: ", mid)
            return mid
        elif arr[mid]<element:
            low=mid+1
        else:
            high=mid-1

    return "Element not found"







lst=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    x=int(input("Enter {} element: ".format(i+1)))
    lst.append(x)
ele=int(input("Enter the element to be searched: "))
searchedElement=binary_search(lst, ele)

print("Element found at position: ", searchedElement)

