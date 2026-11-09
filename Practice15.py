## Create a new file "practice1.txt" using python. Add the following data in it:
# Hi everyone
# we are learning File I/O 
# using Java.
# I like programming in Java.
with open("practice.txt", "w") as f:             # If we take write mode, file is automatically created.
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java.\nI like programming in Java.")

with open("practice1.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java.\nI like programming in Java.")


## WAF that replaces all occurrences of "java" with "python" in above file.
with open("practice1.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

# Overwrites the original data
with open("practice1.txt", "w") as f:
    f.write(new_data)


## Search if the word "learning" exists in the file or not.
def check_for_word():
    word = "learning"
    #word1 = "xlearning"     # "NOT FOUND"
    with open("practice1.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("FOUND")
        else:
            print("NOT FOUND")

check_for_word()


## WAF to find in which line of the file does the word "learning" occur first.
# Print -1 if word not found.
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice1.txt", "r") as f:
        while data:   # while loop me jub tak koi valid value hai tub tak woh loop chalega.
            data = f.readline()   # jub readline se empty string return hote h toh woh valid value nhi hai!!
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1
print(check_for_line())

# From a file containing numbers separated by comma, print the count of even numbers.
# 1, 2, 4, 45, 55, 86, 76, 98, 101
# how you will do it ?
# 1) Individual number ko extract kro
# 2) Parse / Casting to integer.
with open("practice2.txt", "r") as f:
    data = f.read()
    print(data)   

    num = ""
    for i in range(len(data)):
        if (data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]
    if num:
        print(int(num))

# with open("practice2.txt", "r") as f:
#     data = f.read()
#     print(data)   

#     count = 1
#     for i in range(len(data)):
#         if (i % 2 == 0):
#             print(count) 
#             i += 1          
#         else:
#             num += data[i]


# using split()
count = 0
with open("practice2.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    print(nums)
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)
