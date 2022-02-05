# Tuples

# Tuple: Sequence of values, indexed by integers
# Tuples are immutable


# CREATING A TUPLE
# Tn = O(1), Sn = O(N)
t = ('a', 'b', 'c', 'd', 'e')

# for single element tuple use comma at the end o/w it will consider it as a string
t1 = ('a',)

# creating tuple using tuple()
t2 = tuple('abcde') 

# empty tuple
t3 = tuple()


# ACCESSING TUPLE ELEMENTS
print(t[1])
print(t[-1])

# SLICING
print(t[1:3])
print(t[:])

# NOTE: tuples are immutable, hence t[2] = 'c' can't be done


# TRAVERSING THROUGH A TUPLE
# Tn = O(N), Sn = O(1)
t = ('a', 'b', 'c', 'd')

for i in range(len(t)):
    print(t[i)) 


# SEARCHING FOR AN ELEMENT IN TUPLE
print('b' in t)

# Linear search
# Tn = O(N), Sn = O(1)
def searchTuple(pTuple, elem):
    for i in pTuple:
        if i == elem:
            return pTuple.index(i)
    return "element does not exist"

print(searchTuple(t, 'c'))

# NOTE: Tulpes are immutable, so the result of operations is a new tuple, just like strings



# OPERATIONS

# + operator
t1 = (1, 3, 4, 2, 5)
t2 = (1, 5, 4, 4, 6)
print(t1 + t2) # (1, 3, 4, 2, 5, 1, 5, 4, 4, 6)

# * operator
print(t1 * 3) # (1, 3, 4, 2, 5, 1, 3, 4, 2, 5, 1, 3, 4, 2, 5)

# in operator
# returns True, if elem exist inside tuple, else returns false
print(4 in t1)

# METHODS

# count(value)
print(t1.count(2)) # 1

# index(value)
print(t1.index(4)) # 2

# len 
print(len(t1)) # 5

# max
print(max(t1)) # 5

# min 
print(min(t1)) # 1

# tuple(): covert list to tuple
print(tuple([1, 3, 4, 2, 5]))
