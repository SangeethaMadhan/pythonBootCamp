# Open a file with its file name.
# To read the file use readlines().
# Create a variable and store the file to access
# Remove the extra lines or white spaces using strip()
# Convert string to integer.
# Print the unsorted array.
# Sort the array.
# Return the sorted file to sorted.txt file by adding new lines and converted into string

file = open("numbers.txt",'r') # Open numbersFile.txt and read the file

array = file.readlines() # Setting a variable(array) to store the file
print("Text file: ",array) # Print the array

for i in range(0,len(array)):

    print("Array before strip",array[i])

    array[i]=array[i].strip() # Removing empty lines
    print("Array after strip",type(array[i]),array[i])
    
    array[i]=int(array[i]) # Converting string of elements into integer
    print("Convert string to integer",type(array[i]),array[i])

print("Array:",array) # Print the interger array

start_index = 0 # assign start index as 0
end = len(array)-1

while start_index<end:
    minimum = start_index # assign start_index to minimum 0th index
    i = start_index + 1 # updating start index(min_index)

    while i<len(array):
        if array[minimum] > array[i]: # by comparing minimum value with other elements find minuimum value
            minimum = i
            
        else:
            minimum = minimum

        i = i + 1

    array[start_index], array[minimum] = array[minimum], array[start_index] # swapping minimum value with the start_index value

    start_index = start_index + 1 # updating start_index

print("Sorted Array:", array) # Sorted array

file_sorted = open("sorted.txt", 'w') # Write the sorted array to the sorted.txt file

for j in array:
      file_sorted.write(str(j)+'\n') # Adding new lines and converting interger into string
file_sorted.close()

