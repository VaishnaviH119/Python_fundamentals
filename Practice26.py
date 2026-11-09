# 11. Write a program to find the missing number in an array containing numbers from 1 to n. 

# missing number in an array ---> can be any number
# suppose we have n = 5, and the array is [1,2,3,4,5], and if we remove 3, 
# the array becomes, [1,2,4,5], and the missing number is 3


def find_missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum  = sum(arr)
    missing_number = expected_sum - actual_sum 
    return missing_number

print(find_missing_number([1, 2, 4, 5], 5))