#bubble sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1): #n-i-1 is used to avoid the comparison of already sorted elements in the list which already comes in the last of each iteration
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

lst = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    x = int(input("Enter {} element: ".format(i+1)))
    lst.append(x)

sorted_lst = bubble_sort(lst)
print("Sorted list is: ", sorted_lst)