# Print numbers from 1 to 100
i = 1
while i <= 100:  # stopping condition 
    print(i)
    i += 1

# Print numbers from 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1

# Print the multiplication table of a number n
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n * i)
    i += 1

# Print the elements of the following list using a loop:
#  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# traversing a list
idx = 0
while idx < len(nums):
    print(nums[idx])   # nums[0], nums[1], nums[2], ....
    idx += 1

heroes = ["Ironman", "Batman", "Superman", "Thor"]

i = 0
while i < len(heroes):
    print(heroes[i])
    i += 1


# Search for a number x in this tuple using loop:
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)

x = 36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("Found at index", i)
        break   # Here added break, to terminate from the loop, when we found the element for the first time.
    else:
        print("Finding...")
    i += 1


# Practice using for loop 

# Print the elements of the following list using a loop:
#     [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for num in nums:
    print(num)


# Search for a number x in this tuple using loop:
#     [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49]

x = 49 

idx = 0
for num in nums:
    if(num == x):
        print("x found at", idx)
    idx += 1



nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49]

x = 49 

idx = 0
for num in nums:
    if(num == x):
        print("x found at", idx)
        break
    idx += 1


# Practice using range function and for loop together   

# Print numbers form 1 to 100
for i in range(1, 101):
    print(i)

# Print numbers from 1 to 10 with a gap of 2
for i in range(1, 11, 2):
    print(i, end=" ")  

# Print numbers from 100 to 1.
for i in range(100, 0, -1):
    print(i, end=" ")   

# Print multiplication table of a number n.
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n * i)

# WAP to find the sum of first n natural numbers. (using while loop)
n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("Sum of first", n, "natural numbers is:", sum)


# Using for loop
n = int(input("EEnter a number: "))
sum = 0
for i in range(1, n+1):
    sum += i
print("Sum of first", n, "natural numbers is", sum)


# WAP to find the factorial of first n natural numbers. (Using for loop)

# Visualize factorial of a number n as the product of all natural numbers from 1 to n.
# 5 ! = 1 * 2 * 3 * 4 * 5 = 120 
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial of", n, "is", fact)

# Using while loop 
n = int(input("ENter s number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial of", n, "is", fact)