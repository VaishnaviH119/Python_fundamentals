# 10. Write a program to count the frequency of each character in a given string. 

# string = "abracadabra"
# frequency of each character 
# Suppose, we need to find freq of a   
# we can use various methods ---> hashmap, frequncy array 

def char_frequency(txt):
    freq = {}
    for char in txt:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

char_count = char_frequency("abracadabra")
print(char_count)