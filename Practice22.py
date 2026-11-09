# 7. Write a program to print the first n numbers of the Fibonacci series. 

# first n numbers 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 

# Iterative version
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter the number of Fibonacci terms: "))
fibonacci(n)


# Recursive version 
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

n = int(input("\nEnter the number of Fibonacci terms: "))
for i in range(n):
    print(fib(i), end=" ")