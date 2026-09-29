def cal_sum(a, b):   # Function definition with parameters a and b that takes two numbers as inout and return their sum.
    return a + b    

sum = cal_sum(5, 10)  # Calling the function with arguments 5 and 10, and storing the result in variable 'sum'.
print(sum)            # Output: 15


def greet():
    print("Hello, welcome to Python programming!")    # Function definition without parameters that prints a greeting message.

greet()
Output = greet()   # Calling the function and storing the return value in a variable 'Output'. 
print(Output)     # Since the function does not return anything, Output will be None. Output: None

def greetings(name):     # Function definition with a parameter 'name' that takes a string input and print a personalized greeting message.
    print("Hello " + name + ", Welcome to Python programming!")
    print("Hello" , name , ", Welcome to Python programming!")

# + operator is used to concatenate strings, 
# , operator is used to separate arguments in print() and it automatically adds a space between the arguments.

greetings("Vaishnavi")     # Calling the function with argument "Vaishanvi" to print a personalized greeting message.

# Average of two numbers using a function
def average_2(num1, num2):
    return (num1 + num2) // 2   # Using floor division(Integer Division) to return the average.
   
avg = average_2(10, 20)    # Calling the function with arguments 10 and 20, and storing the result in variable 'avg'.
print(avg)                 # Output: 15

# Average of two numbers using a function
def average_2(num1, num2):
    return (num1 + num2) / 2    # Using normal division (floating-point division) to return the average.

avg = average_2(10, 20)    # Calling the function with arguments 10 and 20, and storing the result in variable 'avg'.
print(avg)                 # Output: 15



# Average of three numbers 
def average_3(a, b, c):
    sum = a + b + c
    return sum / 3

avg = average_3(10, 20, 30)
print(avg)      # Output: 20.0


# Built-in functions
# 1. print() - used to display output on the console.
print("Hello, World!") 
print("Hello","World", sep="@", end="!!!\n")  
# sep is used to specify the separator between the arguments and
# end is used to specify what to print at the end of the output. 
# By default, sep is a space and end is a newline character.

# 2. Input() - used to take input from the user.
name = input("Enter your name: ")   # Taking input from the user and input() function return a string value which is stored in variable 'name'.
num = int(input("Enter a number: "))    # Taking input from the user and converting it to an integer using int() function before storing it in variable 'num'.

# 3. len() - 

    

