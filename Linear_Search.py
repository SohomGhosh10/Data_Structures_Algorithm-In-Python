
            
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target element if found
    return -1  # Return -1 if the target element is not in the list

# Example usage:
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
target_element = 6
result = linear_search(my_list, target_element)

if result != -1:
    print(f"{target_element} found at index {result}")
else:
    print(f"{target_element} not found in the list")
