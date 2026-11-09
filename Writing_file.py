# WRITING TO A FILE
f = open("demo.txt", "w")  # Overwrites the original text with the new text.
f.write("I want to learn Javascript tomorrow. 123")  
f.close()

f = open("demo.txt", "a")  # Appends text into the file 
f.write("Then I will move to reactJS.")
f.write("\nAfter that nodeJS.")


# If we open a file through "w" or "a" then it will create an empty file which doesn't even exist.
f = open("sample.txt", "w")
f = open("sample2.txt", "a")

f = open("sample.txt", "r+")
f.write("abc")
print(f.read())
f.close()

f = open("sample2.txt", "w+")  # Truncates 
# f.write("abc")
print(f.read())
f.write("abc")
f.close()

