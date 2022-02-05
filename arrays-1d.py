# Arrays

# 1D Array: An array with a bunch of values having been declared with a single index
# 2D Array: An array with a bunch of values having been declared with double index

# In python, array is not a built in data structure, so we will import the array module
from array import *

# CREATING AN ARRAY
# arrayName = array(typecode, [initializers])
# Tn = O(1), Sn = O(n)

# Integer type array
arr1 = array('i', [1, 2, 3, 4, 5])

# float type array
arr2 = array('f', [1.4, 3.5, 3.7, 8.4])

# empty array
arr3 = array('i')


# LENGTH OF AN ARRAY
print(len(arr1))


# ACCESSING ARRAY ELEMENTS
# arrayName[index]
print(arr1[2])
# Tn = O(1), Sn = O(1)


# GET THE BUFFER INFO OF AN ARRAY
print(arr1.buffer_info())


# ADDING ELEMENTS TO AN ARRAY

# append(value): adds an element at the end of array
arr1.append(6)
print(a)

# extend(array): extends the array by specified elements
arr1.extend([4, 8, 9])
print(a)

# insert(index, value): inserts an element at a specified index
arr1.insert(3, 7)


# REMOVING ELEMENTS FROM AN ARRAY

# remove(value): removes the element of specified value
arr1.remove(3)

# pop(index): removes the element of specified index
arr1.pop(0)

# Note:
# Time complexity of adding/ removing element at the start (index 0) of an array = O(N)
# Time complexity of adding/ removing element at the end = O(1)
# Time complexity of adding/ removing element anywhere in the middle = O(N)


# TRAVERSING AN ARRAY
def traverseArray(array):
    for i in array:
        print(i)

traverseArray(arr1)

# Time complexity for traversing an array = O(N)
# Space complexity for traversing an array = O(1)


# SEARCHING FOR AN ELEMENT IN ARRAY
def searchArray(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return "The element does not exist in the array"

print(searchArray(arr1, 3))
# Time complexity for this way of searching an element in array = O(N)
# Space complexity = O(1)

# SLICING AN ARRAY
# arr1 is [1, 2, 3, 4, 5]
print(arr1[0:2])      # [1, 2]
print(arr1[0:-2])     # [1, 2, 3]
print(arr1[0:4:2])    # [1, 3]
print(arr1[:3])       # [1, 2, 3]
print(arr1[2:])       # [3, 4, 5]


# ARRAY CONCATENATION
a1 = array('i', [1, 2, 3, 4])
a2 = array('i', [5, 6, 7, 8])
c = array('i')
c = a1 + a2
print(c)


# NUMBER OF OCCURANCE OF AN ELEMENT
# arrayName.count(value)
print(arr1.count(2))


# ADD ITEMS FROM LIST TO AN ARRAY 
# fromlist()
tempList = [20, 21, 22]
arr4 = array('i')
arr4.fromlist(tempList)
print(arr4)

# Array -> List
print(arr4.tolist())

# ARRAY TO STRING CONVERSION
a5 = array('i', [4, 5, 6])
strTemp = arr5.tostring()
print(strTemp)
