# 3. Write a program to find the largest and smallest elements in an array 

# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# size = int(input("Enter the size of the array: "))
# array = list(map(int, input("Enter the elements of the array: ").split()))
# largest = array[0]
# smallest = array[0]

# for i in range(len(array)):
#     if array[i] > largest:
#         largest = array[i]
#     elif array[i] < smallest:
#         smallest = array[i]

# print("Largest element in the array is:", largest)
# print("Smallest element in the array is:", smallest)


def find_largest_smallest(arr):
    largest = arr[0]
    smallest = arr[0]

    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
        elif arr[i] < smallest:
            smallest = arr[i]

    return largest, smallest   # Python groups those values into a tuple, like (10, 1) 
                               # and return that tuple to the caller.
                               # The caller can unpack the tuple into two variables, the largest and smallest, using the assignment statement.
# So largest gets 10 and smallest gets 1. Then you can print each one with a label.
largest, smallest = find_largest_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])     # This is the assignment statement.
print("Largest Element:", largest)
print("Smallest Element:", smallest)
