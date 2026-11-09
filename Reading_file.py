# READING A FILE
f = open("demo.txt", "r")
data = f.read()     # read entire file
print(data)
print(type(data))

data = f.read(5)   # I am 
print(data)
f.close()
# if we use f.read() once and read all the data of the text file,
# then if we use readline, it won't print anything as all the data is already been read.

# To use readline, we need to close the file and then open it once again and then we can use readline.
f = open("demo.txt", "rt")   # t denotes text file and it is default, if we don't write t, still it takes as a text file.
line1 = f.readline()   # reads one line at a time.
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()    # Print nothing as all the data has been read line by line.
print(line3)

f.close()







