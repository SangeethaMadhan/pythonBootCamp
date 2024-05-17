# Sort the given array using Quick Sort method.
# Consider an array and its middle value of array as pivot value
# For thet find the pivot index value by adding first index and last index value and divided by 2, thus middle value index can be found.
# Step 1: Swapp all the values that are lesser than the pivot value to the left side of array.
# Then swapp all the values that are higher than the pivot value to the right side of array.
# Step 2: Sort the values that are present left side of the pivot value.
# Then sort all the values present at the right side of pivot value.
# Return the sort array.


def quickSort(array,low,high):
    # Rearrange values before pivot as smaller and values after pivot as larger elements.
    # Assign arr[(low+right)//2] as pivot.

    if low >= high:
        return
    
    pivot = array[(low+high)//2]

    i = low
    j = high

    while i<j:

        # find the first left index that needs to be swapped
        while array[i] < pivot:
            i = i+1

        # find the first right index that needs to be swapped
        while array[j] > pivot:
            j = j-1

        array[i], array[j] = array[j], array[i]

    pivot_index = i
    
    # Sort left side
    quickSort(array, low, pivot_index-1)
    # Sort right side
    quickSort(array, pivot_index+1, high)

array=[4,9,3,1,7,8,6,2,10]
quickSort(array,0, len(array)-1)
print(array)
