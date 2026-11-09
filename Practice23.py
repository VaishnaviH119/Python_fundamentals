# 8. Write a program to find the factorial of a given number using recursion. 

# factorial of a given number 
# 5! = 5 x 4 x 3 x 2 x 1  => 120 
# n! = n x (n-1) x (n-2)

# Recursive version
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))

### DRY RUN
# if case => n == 0 or n == 1  => 1
# n = 5
# else case :=
# 5 * factorial(4)  => 5 * 24 => 120
# 4 * factorial(3)  => 4 * 6 => 24
# 3 * factorial(2)  => 3 * 2 => 6
# 2 * factorial(1)  => 2 * 1 => 2
# 1 * factorial(0)  => 1 * 1 => 1


# Iterative version
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))


### DRY RUN
# n = 5
# result = 1
# range -> 1 to n + 1 => 1 to 6  (range function hai toh 6 include nhi hoga, it will go till 5 only).

# result = result * i

# result = 1 * 1
# result = 1 * 2 
# result = 2 * 3 => 6
# result = 6 * 4 => 24
# result = 24 * 5 => 120

