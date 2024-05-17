# Python program in-place Merge Sort
# Objective: Write a program to sort an array having two sorted subarrray using in-place sorting method.
# Consider an array having two sorted subarray split them as left and right array.
# Define the inplace function and write body of the function.
# Name the first index value of left side array as "first".
# Name the first index value of right side array as "second"
    # Compare the first and second.
    # if array[first] <= array[second]:
    # first = first + 1
    # else save second in temp ie. temp = array[second] and assign second index to i ie. i = second
# Increment the first and second index values till first < second and second <= end.
# Define the array to be sorted and call the inplace function
# Print the sorted array


def inplace(array, first, second, end): 

    while first < second and second <= end:

        if array[first] <= array[second]: # comparing both values
            first = first + 1
        else:
            temp = array[second] # if second is less tha first then save it in temp and right shift other array elements
            i = second

            while i > first:
                array[i] = array[i - 1] # shifting all the elements till first = first + 1
                i = i - 1
                
            array[first] = temp

            first = first + 1
            second = second + 1

array = [3, 5, 11, 2, 7, 20]
end = len(array)-1

inplace(array, 0, 3, end)

print(array)