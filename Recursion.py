# def show(n):
#     if n == 0:
#         return 
#     print(n)
#     show(n-1)
# show(5)

# Infinite Recursion (Without Base Case)
# def show(n):
#     # if n == 0:
#     #     return
#     print(n)
#     show(n-1)
# show(3)

# Call Stack and FLow of Execution in Recursion
def show(n):      # This function demonstrates a recursive call and the flow of execution.
    if n == 0:
        return
    print(n)
    show(n-1)
    print("Back to", n)    # This line will be executed after the recursive call returns.

show(5)

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1) 

print(factorial(4))