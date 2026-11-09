with open("demo1.txt", "r") as f:
    data = f.read()
    print(data)

with open("demo1.txt", "w") as f:
    f.write("new data")