def Binary_Search(arr , target):
    low = 0
    high = len(arr) - 1
    
    if low > high:
        return -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            low = mid + 1
        
        else:
            high = mid - 1
            
    return -1

my_list = [1 , 3 , 5 , 7 , 9 , 11 , 13 , 15 , 17 , 19]
target_element = 11

result = Binary_Search(my_list , target_element)


if result != -1:
    print(f"{target_element} lies in the list of index {result}")
else:
    print(f"{target_element} is not found int the array")