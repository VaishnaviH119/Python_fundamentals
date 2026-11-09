str1 = "This is a string."
str2 = 'My name is Vaishnavi'
str3 = """This is another string"""

print(str1)
print(str2)
print(str3)

print("Someone's world")
print('Someone"s World')

# print("Someone"s Account")  # Error
# print('Someone's Book')  # Error

# It will give an error
#str1 = "this is new string.
#i love python..."

str1 = "This is new String.\nI am learning new things."
print(str1)

str2 = "I am getting intelligent and smarter day by day.\tBut it's taking so mauch time, for things to unfold."
print(str2)

a = "apna"
b = "college"
final_str = a + b
print(final_str)

a = "Tomorrow"
len_a = len(a)
print(len_a)

b = "Will be Better"
len_b = len(b)
print(len_b)

final_str = a + " " + b
print(final_str)
length = len(final_str)
print(length)


str = "apna college"
#str[4] = "@"   # Error -> we cannpt assign(manipulate) string positions.
print(str[0])
print(str[1:4])
print(str[5:12])
print(str[5:len(str)])
print(str[5:])   # [5:len(str)]
print(str[:4])   # [0:4]

str = "apple"
print(str[-5:-2])
print(str[-3:-1])

str4 = "I am studying python with apna college"
print(str4.endswith("ege"))  # Returns true if the string ends with substring.
print(str4.endswith("app"))

str5 = "i am studying python with apna college"
# changes in the copy of a string, original string remains unaffected.
print(str5.capitalize())    # Capitalize 1st character
print(str5)
#Modifications in the original string
str5 = str5.capitalize()    # Make changes in the original string.
print(str5)

print(str5.replace("o", "a"))  # replaces all occurrences of old to new.
print(str5.replace)

print(str5.find("o"))   # Gives the first occurrence 
print(str5.find("with"))  # returns 1st index of 1st occurrence
print(str5.find("from"))
print(str5.find("Q"))

print(str5.count("o"))   # Counts the occurrence of the substring.
print(str5.count("from"))
