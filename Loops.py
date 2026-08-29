# # Loops are used to repeat instructions
# # while loops

# # while -> jub tak condition true hai tub tak print kro...

# # while True:
# #     print("kem cho?")

# count = 1
# while count <= 5:
#     print("Kem Cho?")
#     count += 1
# print(count)


# # # i = 1
# # # while i<= 100000:
# # #     print("Anyeonghaseo", i)
# # #     i += 1

# # Print numbers from 1 to 5
# i = 1
# while i <= 5:
#     print(i)
#     i += 1
# print("Loop ended")

# # Reverse 
# i = 5
# while i >= 1:
#     print(i, end=" ")
#     i -= 1
# print("\nReverse Loop ended")

# # Infinite Loop
# # i = 5
# # while i < 6:
# #     print(i)
# #     i -= 1
# # print("Infinite Loop")




# # Break:
# #    Break is used to terminate the loop when encountered.

# i = 1
# while i <= 5:
#     print(i)
#     if (i == 3):
#         break
#     i += 1
# print("End of Loop")


# # Continue:

# i = 0
# while i<=5:
#     if (i == 3):
#         i += 1        # This line will increments i to 4.
#         continue   # Skips the current iteration and moves to next by incrementing.
#     print(i)           # Steps after continue, will be skipped.
#     i += 1
# print("Loop ended")


# i = 1
# while i <= 10:
#     if (i%2 == 0):
#         i += 1         # for incrementing to i = 3
#         continue
#     print(i)    # this statement will be skipped by the continue keyword for even numbers
#     i += 1      # this will also be skipped.

# i = 1
# while i <= 10:
#     if (i%2 != 0):
#         i += 1         # for incrementing to i = 3
#         continue
#     print(i)    
#     i += 1





# # For Loops

# nums = [1, 2, 2, 3, 4, 4, 5]
# for val in nums:
#     print(val)

# veggies = ["Okra", "Potatoes", "Tomatoes", "Brinjal"]
# for v in veggies:
#     print(v)

# nums = (1, 2, 3, 4, 4, 5)
# for num in nums:
#     print(num)

# str = "Python"
# for char in str:
#     print(char)


# stri = "Apnacollege"

# for char in stri:
#     print(char)
# else:
#     print("END")

# # for char in stri:
# #     print(char)
# #
# # print("END")

# # Why there is a need of else when we can print the ending statement without else.
# # Else is used when break statement is included.

# str = "apnacollege"
# for char in str:
#     if(char == 'o'):
#         print("o found")
#         break
#     print(char)
# else:              # This statement is not executed.
#     print("END")   


# str = "apnacollege"
# for char in str:
#     if(char == 'o'):
#         print("o found")
#         break
#     print(char)
# print("END")    # This statement is executed 



# #Range function
# print(range(5))   # range object
# print(list(range(5)))   # Type casting to list

# seq = range(5)

# print(seq[0])  
# print(seq[1])
# print(seq[2])

# for i in seq:
#     print(i)

# for i in range(10):   # Instead of creating a range object which is stored in seq,
#     print(i)            # we can directly use the range function in the for loop.
    
# # range object creates a sequence of numbers from 0 to n-1, where n is the argument passed to the range function.
# # It is a memory efficient way to generate a sequence of numbers, as it does not store them in a list, but rather generates them on the fly when requested.

for i in range(10):         # range(stop) -> 0 to stop-1
    print(i, end=" ")  
    # end = " " is used to print the numbers in the same line with a space in between.

for i in range(1, 11):   # range(start, stop) -> start to stop-1     
    print(i, end=" ")

for i in range(1, 11, 2):
    print(i, end=" ")       # range(start, stop, step) -> start to stop-1 with a gap of step. 
# Here we are printing odd numbers from 1 to 10 with a step of 2.

for i in range(2, 101, 2):
    print(i, end=" ")      # Here we are printing even numbers from 2 to 100 with a step of 2.

for i in range(1, 100, 2):
    print(i, end=" ")      # Here we are printing odd numbers from 1 to 99 with a step of 2.

for i in range(10, 0, -1):
    print(i, end=" ")   # Here we are printing numbers from 10 to 1 with a step of -1, 
                        # which means we are decrementing the value of i by 1 in each iteration.
print("Loop ended")  


# Pass Statements
# --> Pass is a null statement in Python.
# --> It is used when a statement is required syntactically but you do not want any command or code to execute.
# --> It is often used as a placeholder for future code or to create minimal classes or functions.
# --> When the pass statement is executed, nothing happens, and the program continues to the next statement.
# --> It is commonly used in situations where you want to define a function or a class but haven't implemented it yet, allowing the code to run without errors.
# --> It can also be used in loops or conditional statements where you want to do nothing for a specific case.
# --> The pass statement is a way to indicate that you have intentionally left a block of code empty, and it serves as a placeholder for future implementation.
# --> Example of using pass in a function definition:

def future_function():
    pass  # This function does nothing for now, but it can be implemented in the future.
print("This is a placeholder function that does nothing.")

# for i in range(5):
#     # empty loop body
# print("This will cause an IndentationError because the loop body is empty, but we can use pass to avoid that error.")

# loop body cannot be empty, if it is empty, it will raise an IndentationError. To avoid that error, we can use pass statement in the loop body.

# Example of using pass in a loop:
for i in range(5):
    if i % 2 == 0:
        pass  # This will skip the even numbers and do nothing for them.
    else:
        print(i)  # This will print the odd numbers from 0 to 4, while the even numbers will be ignored due to the pass statement.

