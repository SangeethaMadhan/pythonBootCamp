# a1=3,5,8,9    a2=4,7,8,10    a3=[]
# a3=3   a1=5,8,9   a2=4,7,8,10
# a3=3,4   a1=5,8,9   a2=7,8,10
# a3=3,4,5   a1=8,9   a2=7,8,10
# a3=3,4,5,7   a1=8,9   a2=8,10
# a3=3,4,5,7,8    a1=9   a2=8,10
# a3=3,4,5,7,8,8   a1=9   a2=10
# a3=3,4,5,7,8,8,9   a1=[]  a2=10
# a3=3,4,5,7,8,8,9,10  a1=[]  a2=[]

# arr1=1,3,4,5
# arr2=2,4,6,8
# arr3=[]
# i, j, k = 0, 0, 0
# while i<len(arr1) and j<len(arr2):
    # if arr1[i] < arr2[j]:
        # arr3[k] = arr1[i]
        # i=i+1
        # k=k+1
    # else:
        # arr[k] = arr2[j]
        # j=j+1
        # k=k+1
# print(arr3)


arr1 = [3, 5, 6, 10]
arr2 = [1, 2, 7, 8, 11, 12]
arr3 = []
i = 0
j = 0
k = 0
    
while i < len(arr1) and j < len(arr2) and k < len(arr1 + arr2):
    if arr1[i] < arr2[j]:
        arr3[k] = arr1[i]
        k = k + 1
        i = i + 1
    else:
        arr3[k] = arr2[j]
        k = k + 1
        j = j + 1
        
while i < len(arr1):
    arr3[k] = arr1[i]
    k = k + 1
    i = i + 1
    
while j < len(arr2):
    arr3[k] = arr2[j]
    k = k + 1
    j = j + 1

print(arr3)