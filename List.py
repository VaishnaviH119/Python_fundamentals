marks1 = 94.4
marks2 = 87.5
marks3 = 78.6
marks4 = 66.4
marks5 = 49.8

marks  = [94.4, 87.5, 78.6, 66.4, 49.8]   # List in python
print(marks)
print(type(marks))

print(len(marks))
print(marks[0])
print(marks[1])

student = ["Karan", 85.6, 17, "Delhi"]
print(student)

# In string and tuple, we can not change the value of the element 
# but in list we can change the value of the element as list is mutable.
str = "Hello"
#str[0] = "y"
print(str[0])

print(student[0])
student[0] = "arjun"
print(student)

#print(student[5])  # List index out of range -> error

# List Slicing 
marks = [85, 94, 76, 63, 48]
print(marks[1:4])
print(marks[1:])
print(marks[:5])   # :5 for getting the last most index.
print(marks[-3:-1])   # [76, 63]

#List Methods

list = [2, 3, 5]
list.append(6)
print(list)
# this is called as mutating the list as we are modifying or changing the elements in the list.
print(list.append(4))

print(list.sort())         # list.sort() -> Method, which gives output as none.
print(list)  

print(list.sort(reverse=True))  # Does not print the list but rather give output as none
print(list)


listi = ["litchi", "Banana", "Apple", "Grapes"]
print(listi.sort())
print(listi.sort(reverse=True))   # prints list in a reberse order.
print(list)

listi2 = ['a', 'c', 'f', 'x', 'k', 'b']
listi2.append('v')
print(listi2.sort())
print(listi2)
print(listi2.sort(reverse=True))
print(listi2)


listo = [1, 3, 5, 6, 9, 0]
listo.reverse()
print(listo)

listo.insert(3, 8)
print(listo)

listi3 = [2, 1, 4, 3, 5, 4]
listi3.remove(4)  # removes the first occurrence of that particular element
print(listi3)
listi3.pop(1)    # removes element at index 1
print(listi3)