# 12. Given an array of integers and a target value, write a program to find two numbers whose sum equals the target value. 

# Example: [2, 7, 11, 15], target = 9, output: [2, 7]

# Main Logic:
# Instead of checking all pair manually, remember what you have seen so far. 
# For each number, check if the complement (target - number) exists in the seen numbers. 
# If it does, return the pair. 
# If not, add the number to the seen numbers.

def two_nums(arr, target):
    nums = {}              # stores the seen numbers of the array
    for num in arr:
        complement = target - num
        if complement in nums:
            return [complement, num]
        nums[num] = True                 # stores the number in the dictionary
    return None                   # returns None if no pair is found

# TC -> O(n) 
# SC -> O(n)  because we are storing the seen numbers in a dictionary.