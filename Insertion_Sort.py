def insertionSort(arr):
    n = len(arr)
    
    for i in range(n):
        current = arr[i]
        j = i - 1
        
        while arr[j] > current and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    
my_list = [13 , 15 , 64 , 26 , 48 , 78]
insertionSort(my_list)
print("Sorted list is",my_list)