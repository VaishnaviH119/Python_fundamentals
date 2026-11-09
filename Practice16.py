# 1. Write a program to reverse a string without using a built-in reverse function.
# string = input("Enter a string:")
# newString = ""
# for i in range(len(string)-1, -1, -1):
#     newString += string[i]
# print("Reversed string is:", newString)



def reversed_string(text):
    reversed_str = " "
    for i in range(len(text)-1, -1, -1):
        reversed_str += text[i]
    return reversed_str

newString = reversed_string("Hello World")
print("Reversed String is:", newString)

