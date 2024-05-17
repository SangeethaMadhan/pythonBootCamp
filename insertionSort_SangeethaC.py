# Objective: To Arrange the array elements in ascending order - using insertion method.
# Find the first minimum value in the array.
    # Compare the first two numbers in the array and assign smallest number as minimum.
    # If the minimum is greater than nearest element, store the nearest element as minimum 
    # If the minimum is smaller than nearest element, minimum = minimum
    # Likewise compare the minimum with every elements in an order.
    # Then first minimum value can be found.
# Minimum value stored in the variable minimum.
# Minimum index stored in the variable min_index.
# Right shift all the values present before minimum.
    # list[minimum] = list[minimum-1]
    # list[minimum-1] = list[minimum-2]
    #.....
    # list[start_index+1] = list[start_index]

# Finally move the minimum value to 1st place (index 0)
# Freeze the 1st value (index 0)
# Increment start index and Repeat the steps upto the final value in the array.

6,8,2,7,1,10 # --> min=1, values present before 1 shifted right once to move 1 to 0th index
1,6,8,2,7,10 # --> min=2
1,2,6,8,7,10 # --> min=6
1,2,6,8,7,10 # --> min=7
1,2,6,7,8,10 # --> min=8
1,2,6,7,8,10 # --> min=10
1,2,6,7,8,10 # Sorted array through insertion


list = [6,8,2,7,1,10]
start_index = 0 # assign start index as 0
end = len(list)-1 # length of list as end

while start_index < end: # loop to run inner loop till start index is not equal to end
    minimum = start_index # assign start_index to minimum
    i = start_index + 1 # updating start index(minimum_index) to run loop

    while i < len(list):
        if list[minimum] > list[i]: #comparing minimum value with near element
            minimum = i # assigning i as minimum index
            
        else:
            minimum = minimum

        i = i + 1 # updating i to check with other values

    a = list[minimum] # assigning minimum value to 'a'

    while minimum != start_index: # looping till start_index + 1
        
        list[minimum] = list[minimum-1] # shifting right - elements before minimum

        print(list[minimum])
        print(minimum)
        print(list)
        
        minimum = minimum - 1 # decrementing mimimum index to shift all the elements before minimum
    
    list[start_index] = a # assign minimum value to start_index

    start_index = start_index + 1 # updating start_index to freeze the found minimum values

print("Sorted list:", list)