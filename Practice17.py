# 2. Write a program to check whether a given string or number is a palindrome.
# string = input("Enter a string or number:")
# for i in range(len(string)//2):
#     if string[i] != string[len(string)-1-i]:
#         print("Not a Palindrome")
#         brk
#     else:
#         print("Palindrome")
#         ea

#                       0 1 2 
# s[0] = 3 - 1 - 0      p o p     
#      = 3 - 1                   0 1 2
#      = 2                       p o p 
# s[1] = 3 - 1 - 1
#      = 2 - 1
#      = 1

def is_palindrome(text):
    for i in range(len(text)//2):
        if text[i] != text[len(text)-1-i]:
            return False
    return True

print(is_palindrome("pop"))
print(is_palindrome("hello"))