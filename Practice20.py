# 5. Write a program to find the second largest element in an array without sorting the array. 


# arr = [2, 1, 4, 6, 3, 5, 9, 8, 7, 10]

# largest element -> 10
# second largest -> 9

# largest > second largest

def second_largest(arr):
    largest = max(arr)
    second = None

    for num in arr:
        if num != largest:
            if second is None or num > second:
                second = num
    return second

second_largest = second_largest([2, 1, 4, 6, 3, 5, 9, 8, 7, 10])
print("The second largest element is:", second_largest)


