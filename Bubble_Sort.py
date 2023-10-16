def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        #Swapping
        
        for j in range(0 , n - i - 1):
            if arr[j] > arr[j + 1]:
                print("Swapping")
                
                arr[j] , arr[j+1] = arr[j+1] , arr[j]

my_list = [13 , 65 , 78 , 25 , 46 , 89]
bubbleSort(my_list)
print("Sorted list is",my_list)
        