# Write a Program to ask the user to enter names of their 3 favourite movies and store them in a list.

movies = []   # Empty List 
movie1 = input("First favourite movie : ")
movie2 = input("Second favourite movie : ")
movie3 = input("Third favourite movie : ")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)

# OR

movies = []   # Empty List 
mov = input("First favourite movie : ")
movies.append(mov)
mov = input("Second favourite movie : ")
movies.append(mov)
mov = input("Third favourite movie : ")
movies.append(mov)

print(movies)

# OR

movies = []
movies.append(input("First Favourite movie : "))
movies.append(input("Second Favourite movie : "))
movies.append(input("Third Favourite movie : "))

print(movies)


# WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)
# [1, 2, 3, 2, 1]           [1, "abc", "abc", 1]
# First make copy of the original list then reverse that list and check 
# the reverse list with the original list 

list1 = ["m", "a", "a", "m"]

copy_list1 = list1.copy()
copy_list1.reverse()

if (copy_list1 == list1):
    print("Palindrome")
else:
    print("Not Palindrome")


# WAP to count the number of students with the "A" grade in the following tuple.
# ["C", "D", "A", "A", "B", "B", "A"]

grade = ("C", "D", "A", "A", "B", "B", "A")

A_graders = grade.count("A")
print(A_graders)

# OR

print(grade.count("A"))


# Store the above values in a list and sort them from "A" to "D".
# Ascending order 
grade = ["C", "D", "A", "A", "B", "B", "A"]   # Values stored in a list
grade.sort()
print(grade)

