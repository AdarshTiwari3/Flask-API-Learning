#Selection sort is similar to bubble sort but it is more efficient than bubble sort. In bubble sort, we compare each element with its adjacent element and swap them if they are in the wrong order. But in selection sort, we select the minimum element from the unsorted part of the list and swap it with the first element of the unsorted part of the list. This process continues until the list is sorted.

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i #it can work with max_index also
        for j in range(i+1, n): #skips the first element
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print("arr:", arr)
    return arr

lst = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    x = int(input("Enter {} element: ".format(i+1)))
    lst.append(x)
sorted_lst = selection_sort(lst)
print("Sorted list is: ", sorted_lst)

# dry run
# Enter the number of elements in the list: 5
# Enter 1 element: 3
# Enter 2 element: 4
# Enter 3 element: 2
# Enter 4 element: 5
# Enter 5 element: 1
# arr: [1, 4, 2, 5, 3]
# arr: [1, 2, 4, 5, 3]
# arr: [1, 2, 3, 5, 4]
# arr: [1, 2, 3, 4, 5]
# arr: [1, 2, 3, 4, 5]
# Sorted list is:  [1, 2, 3, 4, 5]