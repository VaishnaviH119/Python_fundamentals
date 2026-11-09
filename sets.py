collection = {1, 2, 3, 4}
print(collection)
print(type(collection))

collection = {1, 2, 2, 3, 4, 4, "Hello", "world", 6, True, True, False}
print(collection)
print(type(collection))   
print(len(collection))    # total number of unique elements present in the set.

# Duplicate values are not allowed in set, 
# Only unique values
# Unordered -> no order is followed

collection = {}   #  empty dictionary
print(type(collection))

collection = set()    #  This creates an empty set.
print(type(collection))


# Set Methods
# 1) set.add(el)

collection.add(1)
collection.add(2)
collection.add(2)  # Duplicate value will not be considered.
collection.add("Apna college")  
collection.add((1,2,3)) 
# collection.add([1,2,3])    # TypeError : unhashable type : 'list'
#  We can add string, tuple in a set but we cannot add list or dictionary, it will give error.

# 2) set.remove(el)
#collection.remove(6)    # Gives KeyError as the element is not present.
collection.remove(1)
print(len(collection))   # 3

# 3) set.clear()
collection.clear()    # empties the set
print(len(collection))

# 4) set.pop()
collection = {"hello", "world", "Apnacollege", "Python", "Tech"}
print(collection.pop())   # removes a random value
print(collection.pop())
print(collection)


#  5) set.union()

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2))    # {1, 2, 3, 4}
print(set1)
print(set2) 

#  6) set.intersection()

set1 - {1, 2, 3}
set2 = {2, 3, 4}
print(set1.intersection(set2))    # {2, 3}
print(set1)
print(set2) 

































