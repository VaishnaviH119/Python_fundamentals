num = int(input("Enter a number: "))

print(f"The Multiplication table of {num}:")
for i in range(1, 11):       # it will go from 1 to 10, excluding 11.
    print(f"{num * i}")       # Prints every number in new line
    print(f"{num * i}", end=", ")    # Prints every number on one line separating with comma.