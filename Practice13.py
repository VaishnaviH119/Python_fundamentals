# WAP to print the length of a list. (List is the parameter)

fruits = ["apple", "banana", "cherry", "date", "fig"]
companies = ["Google", "Apple", "Microsoft", "Amazon", "Meta", "Tesla", "Netflix", "Adobe", "Intel"]
def list_length(lst):
    print(len(lst))

list_length(fruits)    # Calling the function with the list of fruits to print its length. Output: 5
list_length(companies)    # Calling the function with the list of companies to print its length. Output: 9


# WAP to print the elements of a list in a single line. (List is the parameter)
def print_list(lst):
    for item in lst:
        print(item, end=" ")         # end=" " is used to print the elements in a single line with a space between them.
    print()                       # This print() is used to move to the next line after printing all the elements in the list.

print_list(fruits)
print_list(companies)

# WAP to find the factorial of n. (n is the parameter)
def find_factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    print(factorial)

find_factorial(6)     # Calling the above function to print factorial of 6.  Output: 720

# Objective: To find the factorial of a number using recursion.
def cal_factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * cal_factorial(n-1)

factorial_n = cal_factorial(6)   # Calling the above function to calculate factorial of 6 and storing the result in variable 'factorial_n'.
print(factorial_n)        # Output: 720

# WAP to convert USD to INR. (USD is the parameter)
def usd_to_inr(usd):
    inr = usd * 83
    return inr

usd_amount = float(input("Enter amount in USD: "))   # Taking input from the user for amount in USD and converting it to a floating-point number before storing it in variable 'usd_amount'.
inr_amount = usd_to_inr(usd_amount)   # Calling the above function to convert the user-provided USD amount to INR and storing the result in variable 'inr_amount'.
print(inr_amount)    # Output: 8300

# WAP to take input as a number and if the number is odd then print "Odd" else print "Even". (Number is the parameter)

def check_odd_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
num = int(input("Enter a number: "))
check_odd_even(num)

