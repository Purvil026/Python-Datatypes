# Dictionary

# CREATING A DICTIONARY
# Tn = O(len(dict)), Sn = O(N)
person1 = {"name": "jack", "age": 21}


# ACCESSING DICTIONARY ELEMENTS
# Tn = O(1), Sn = O(1)
print(person1["name"])
print(person1.get("name"))


# CHANGING VALUES
person1["name"] = "linus"
print(person1)


# ADDING NEW KEY-VALUE PAIRS
person1["hobbies"] = ["cricket", "painting"]
print(person1)


# REMOVING ELEMENTS FROM DICTIONARY

# pop(value): removes specified value
person1.pop("name")
print(person1)

# popitem(): removes a random key value pair
person1.popitem()
print(person1)

# clear(): clears the dictionary
person1.clear()
print(person1)

# del
del person1["name"]


# TRAVERSING THROUGH A DICTIONARY
# Tn = O(N), Sn = O(1)
def traverseDict(dict):
    for key in dict:
        print(key, dict[key])

traverseDict(person1)


# SEARCHING FOR AN ELEMENT IN A DICTIONARY
# Tn = O(N), Sn = O(1)
def searchDict(dict):
    for key in dict:
        if dict[key] == value:
            return key, value
    return "The value does not exist"

searchDict(person1)


# COPYING A DICTIONARY
person2 = person1.copy()
print(person2)


# fromkeys()
dict1 = {}.fromkeys([1, 2, 3], 0)
# {1: 0, 2: 0, 3: 0}

# keys(): returns a list of keys
print(person1.keys())

# values(): returns a list of values
print(person1.values())

# update(): adds key-value pairs from one dict to another
newDict = {'a':1, 'b':2, 'c':3}
person1.update(newDict)
print(person1)

# IN operator
# IN only takes keys
print("name" in person1)

# for values
print("jack" in person1.values())

# len 
print(len(person1))

# sorted(iterable, reverse parameter, value)
print(sorted(person1))
print(sorted(person1, reverse = True))
