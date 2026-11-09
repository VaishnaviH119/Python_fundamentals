tup = (2, 1, 3, 4, 2)
print(type(tup))
print(tup[0])
print(tup[1])
#tup[0] = 5   # error


# Empty Tuple
tup = ()
print(tup)
print(type(tup))

# Tuple with single element
tup = (1,)   
print(tup)
print(type(tup))

tup = (1)   # Without comma(,) this single element will be treated as an Integer.
print(tup)
print(type(tup))

tup = ("Hello")   # it will be treated as a string
print(tup)
print(type(tup))

tup = ("Hello",)  # As there is comma is present, it will be treated as tuple.
print(tup)
print(type(tup))

tupe = (1, 2, 3, 4,)
print(tupe)
print(type(tupe))

tupe = (1, 2, 3, 4)
print(tupe)
print(type(tupe))

# Tuple Slicing
tup = (1, 4, 5, 6)
print(tup[1:3])

#Tuple Methods
tup = (2, 3, 6, 7, 3)

#tup = tup.index(6)   # this statement will modify the original string and thus 2 will be assigned in tup.
print(tup.index(6))     # Here in this method index(), 6 is the element and
# the output 2 is the index of that element.
 
tup = tup.count(3)    # This line gives an attribute error, as the tup is replaced by 2
# and it becomes 2.count(3) which fails, thus we will not modify original string.
print(tup.count(3))   # this line doesn't modifies/changes the original string but rather create changes in the copy of the string.

# we can fix this issue by creating a separate variable.
#Fix by keeping the tuple and using a separate variable:
tup = (2, 3, 6, 7, 3)
index_of_6 = tup.index(6)
print(index_of_6)

count_of_3 = tup.count(3)
print(count_of_3)

#Or, if you want to keep using tup, do:
tup = (2, 3, 6, 7, 3)
print(tup.index(6))
print(tup.count(3))

#That will remove the AttributeError.

