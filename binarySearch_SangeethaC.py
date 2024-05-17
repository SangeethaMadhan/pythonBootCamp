# Objective: Program to find an element in an sorted array using binary search method - faster way to find a number in a list.
# First know the total elements, set the left pointer(low) to the first element of the array and the right pointer(high) to the last element.
# Find the mid index value and compare it with value to be found.
    # Mid index value can be found by adding high + low divided by 2.
# If mid index value matches the target (given) value break the loop and return True and its index.
# If the middle element is less than the target value, set the left pointer to the middle index + 1.
# If the middle element is greater than the target value, set the right pointer to the middle index - 1.
# Repeat this process(finding mid_value and setting pointer) till the value found.
# If the target value is not found in the array, return False (-1).


array = [2, 3, 4, 10, 40, 55, 58, 62, 73, 86, 88, 92, 100]
target_value = int(input("The number to be searched: "))

def binary_search(array, target_value): # function definition
    low = 0 # first element of the array
    high = len(array) - 1 # last element of the array
    mid = 0 # intializing mid value as zero
 
    while low <= high:
 
        mid = (high + low) // 2
 
        if array[mid] < target_value:
            low = mid + 1 # If target_value is greater than mid - ignore left side values - move to right side values from mid
 
        elif array[mid] > target_value:
            high = mid - 1 # If target_value is smaller than mid - ignore right side values - move to left side values from mid
 
        else:
            return mid # means target_value is present at middle - value = mid
 
    return -1 # If the value was not present
 
# Function call
value_present = binary_search(array, target_value)
 
if value_present == -1: # if returned value is -1(False) then the input target_value is not present in the array

    print("Element is not present in the array")

else:
    print("Element is present in array, at index: ", value_present) # returns the index of the target_element
  

