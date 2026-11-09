# 9. Write a program to check whether two given strings are anagrams of each other. 
# anagram logic 
# An anagram means:
#   1) Both strings have the same letters
#   2) But the letters may be in a different order
# Example : 
#  yummy  ==  mumyy  
# y u mmY ----> yummY  ----> yummy 
# mu m yY ----> mumyY  ----> mumyy
# yummy == mumyy => {mmuyy == mmuyy) --> Sorted (equal)
#                                          \______ yes ---> they are ANAGRAMS
#                                          \________ no ---> Not ANAGRAMS

def anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)

print(anagram("yummy", "mumyy"))
print(anagram("listen", "silent"))
print(anagram("hello", "mello"))

