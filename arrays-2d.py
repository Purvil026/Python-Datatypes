# 2D Arrays
# 2D Arrays have multiple rows and columns
# a[i][j], where i -> rows, j -> columns


# Importing Numpy
import numpy as np

# CREATING 2D ARRAYS
arr1 = np.array([[2, 5, 3, 1], [4, 2, 7, 5], [8, 5, 9, 2]])
print(arr1)

# Time complexity for creating 2D arrays = O(1), if we do directly like above
# If we create an empty array and then add elements one by one, Tn = O(MN)
# Space complexity for creating 2D arrays = O(MN)


# ACCESSING 2D ARRAY ELEMENTS
# a[i][j]
print(arr1[1][2])
# Tn = O(1), Sn = O(1)


# ADDING ROWS/ COLUMNS TO 2D ARRAYS

# insert(): adds new row or column at a specific index
# newArray = np.insert(arrayName, index, arrayWithNewElements, axis = 0/1)
# axis = 0 (row), axis = 1 (column)
arr2 = np.insert(arr1, 0, [[1, 2, 3, 4]], axis=1)
print(arr2)

# append(): adds new row or column at the end
arr3 = np.append(arr1, [[1, 2, 3, 4]], axis=1)
print(arr2)

# DELETING ELEMENTS FROM 2D ARRAYS
# np.delete(arrayName, index, axis)
arr4 = np.delete(arr1, 0, axis=0)
print(arr4)

# Time complexity for adding/ deleting rows or columns from starting or middle = O(MN)
# Time complexity for adding/ deleting rows or columns from end = O(1)

# TRAVERSING 2D ARRAYS
def traverseArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traverseArray(arr1)

# Time complexity in 2 loops is O(n^2) when both i and j are equal
# When i!= j, Tn = O(MN)
# Sn = O(1)


# SEARCHING FOR AN ELEMENT IN 2D ARRAYS

def searchArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return "found element"
    return "Element not found"

print(searchArray(arr1, 2))
# Tn = O(MN), Sn = O(1)
