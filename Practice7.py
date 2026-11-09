#Write a program to input user's first name and print its length.
first_name = input("Enter your name: ")
length = len(first_name)
print("Length of your name is: ", length)

# Write a Program to find the occurrence of '$' in a string.
str = "Hi, I am $$ symbol at $ 99.99"
print(str.count("$"))

age = 21
if (age >= 18):
      print("Can vote and apply for license ")
      print("Can drive")


light = "green"
if (light == "red"):
      print("STop")
elif (light == "Yellow"):
      print("Look")
elif (light == "Green"):
      print("GO")
else:
      print("Light is broken")

print("end of code")

num = 5 
if (num > 4):
      print("5 is greater")
if (num > 3):
      print("5 is greater")
if (num > 8):
      print("We dont know")


age = 24

if(age >= 18):
      print("can vote")
else:
      print("cannot vote")


# Conditional Statements 
# Grade students based on marks
  # marks >= 90, grade = "A"
  # 90 > marks >= 80, grade = "B"
  # 80 > marks >= 70, grade = "C"
  # 70 > marks, grade = "D"
marks = int(input("Enter marks : "))

if (marks >= 90):
      grade = "A"
elif (marks >= 80 and marks < 90):
      grade = "B"
elif (marks >= 70 and marks < 80):
      grade = "C"
else:
      grade = "D"

print("Grade of the student ->", grade)





# Nesting 
age = 34

if (age >= 18):
      if (age >= 80):
            print("Cannot drive")
      else:
            print("Can drive")
else:
      print("Cannot drive")
