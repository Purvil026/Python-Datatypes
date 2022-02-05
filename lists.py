# Lists

# Lists are mutable
# Lists can have multiple datatypes in the same list unlike an array

# CREATING A LIST
# Tn = O(1), Sn = O(N)
list1 = [1, 2, 3, 4]
list2 = [2.3, 4.5, 9.8]
list3 = [1, 3.4, 's', 'car', 8.9, [3, 4, 6]]
list4 = []
list5 = ['pizza', 'cheese', 'pasta', 'burger']


# LENGTH OF A LIST
print(len(list5))


# ACCESSING LIST ELEMENTS
# Tn = O(1), Sn = O(1)
print(list5[1])
print(list[-2])


# TRAVERSING THROUGH A LIST
# Tn = O(N), Sn = O(1)
for i in list5:
    print(i)


# SLICING [inclusive: exclusive]
print(list5[0:2])
print(list5[1:-2])
print(list5[:2])


# ADDING ITEMS TO THE LIST
# Tn (start, middle) = O(N), Tn(end) = O(1)
# Sn = O(1)

# append(value): adds an element at the end of the list
list5.append('hotdog')
print(list5)

# insert(index, value): adds an element at a specified index
list5.insert(1, 'sandwich')
print(list5)

# extend(list): adds a new list(multiple elements) at the end of the list
list6 = ['frankie', 'milk', 'coke']
list5.extend(list6)
print(list5)


# REMOVING ITEMS FROM THE LIST
# Tn (start, middle) = O(N), Tn(end) = O(1)
# Sn = O(1)

# remove(value)
list5.remove('burger')

# pop(index)
list5.pop(2)
list5.pop() # removes the last element

# delete
del list5[2]
del list[0:2]


# SEARCHING FOR AN ELEMENT IN THE LIST
# Tn = O(N), Sn = O(1)

# in operator
def searchList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return "The value does not exist"

searchList(list5, 'apple')


# LIST OPERATIONS

# + operator (concatenate lists)
a = [1, 2, 3]
b = [2, 4, 6]
c = a + b
print(c) # [1, 2, 3, 2, 4, 6]

#  * operator
a = [0, 1]
a = a * 4
print(a) # [0, 1, 0, 1, 0, 1, 0, 1]

# max(), min()
a = [1, 2, 4, 7, 2]
print(max(a))
print(min(a))

# sum()
print(sum(a))

# finding avg
print(sum(a)/ len(a))

# sort()
a.sort()
print(a)


# MAKING A COPY OF LIST
a = [1, 2, 3]
b = a.copy()
print(b)
