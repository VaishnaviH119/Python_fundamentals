# # 4. Write a program to find duplicate elements in an array. 

# def find_duplicates(arr):
#     seen = set() # to store elements that have been seen   {2, 3, 5, 6, 8, 9}
#     duplicates = [] # to store duplicate elements

#     for num in arr:
#         if num in seen:
#             duplicates.append(num)  # if the number is already in seen, it's a duplicate
#         else:
#             seen.add(num)  # if the number is not in seen, add it to seen
#     return duplicates

# arr = [2, 3, 3, 5, 6, 2, 5, 8, 6, 9]             
# print("Duplicate elements:", find_duplicates(arr))


# NOTE : In Python, a function returns None by default 
#        if it reaches the end without a return statement.

def find_duplicates(arr=()):
    seen = set()
    duplicates = []

    for num in arr:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)

    return duplicates

print(find_duplicates((2, 3, 3, 5, 2)))  # [3, 2]
print(find_duplicates())                 # []


# `arr=()` gives the function a **default value**: an empty tuple. 
# That means if you call `find_duplicates()` without providing an argument, 
# it loops over an empty tuple and returns an empty list (`[]`).

# So these calls are both valid:

# ```python
# find_duplicates((2, 3, 3, 5, 2))  # Uses the tuple you pass in
# find_duplicates()                 # Uses the default empty tuple
# ```

# You could also write `def find_duplicates(arr):` if you want 
# to require callers to provide a sequence every time. 
# For this function, `()` is a safe default because tuples are immutable.


# An immutable object cannot be changed after it’s created. 
# Since () is an empty tuple, the function can safely use it as a default value: 
# the function won’t accidentally add items to it or change it.

# This matters because Python reuses a function’s default object across calls.
# A mutable default, like arr=[], could be changed in one call and affect 
# later calls if the function modifies it. 
# Your function doesn’t modify arr, so a tuple is a safe choice here.







## DRY RUN 
# arr = [2, 3, 3, 5, 6, 2, 5, 8, 6, 9]      # ------> seen ----> unique ---> set()
# # empty collection for seen elements 

# seen = set() # to store elements that have been seen   {2, 3, 5, 6, 8, 9}
# duplicates = [] # to store duplicate elements

# for num in arr:
#     if num in seen:
#         duplicates.append(num)  # if the number is already in seen, it's a duplicate
#         else:
#             seen.add(num)  # if the number is not in seen, add it to seen
            
# print("Duplicate elements:", duplicates)