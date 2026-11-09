#  Store following word meanings in a python dictionary
dictionary = {
    "table" : ["a piece of furniture", "list of facts and figures"],
    #  store two values in the form of list
    "cat" : "a small animal"
}

print(dictionary)



# You are given a list of subjects for students. Assume one classroom is
# requires for 1 subject. How many classrooms are needed for all students.

subjects = {
    "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"
}
# Python -> 3 students of Python -> 1 classroom
# Java -> 3 students of java -> 1 classroom 
# C++ -> 2 students of C++ -> 1 classroom
# javascript -> 1 student of javascript -> 1 classroom 
# C -> 1 student of javascript -> 1 classroom
# Therefore, We require 5 classrooms.
#  Jitne Unique subjects -> Utne classrooms
print(subjects)
print(len(subjects))   # len of this set will be the total number of classrooms.



# WAP to enter marks of 3 subjects from the user and store them in a dictionary.
# Start with an empty dictionary and add one by one. 
# Use subject name as key and marks as value.

# {"phy" : 94, "chem" : 97, "math" : 99}

# dictionary = {}

# marks1 = int(input("Enter physics marks: "))
# marks2 = int(input("Enter chemistry marks: "))
# marks3 = int(input("Enter math marks: "))

# dictionary["Physics"] = marks1
# dictionary["Chem"] = marks2
# dictionary["math"] = marks3

# print(dictionary)


# # OR #

# marks = {}

# x = int(input("Enter phy marks: "))
# marks.update({"Physics" : x})   # key-value pair should be enclosed in curly braces

# x = int(input("Enter chem marks: "))
# marks.update({"Chemistry" : x})   # key-value pair should be enclosed in curly braces

# x = int(input("Enter math marks: "))
# marks.update({"Maths" : x})   # key-value pair should be enclosed in curly braces

# print(marks)


# Figure out a way to store 9 and 9.0 as separate values in the set.
# (You can take help of built-in data types)


values = {9, 9.0}
print(values)     # {9} will be printed as python will treat the integer 9
# and floating point 9.0 as same and therefore will not print it,
# so, it will print only integer value

values = {9, "9.0"}
print(values)

values = {"9", 9.0}
print(values)

values = {
    ("int", 9),
    ("float", 9.0)
}
print(values)   