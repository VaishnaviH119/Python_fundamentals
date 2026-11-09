# Write a recursive function to calculate the sum of first n natural numbers.

def cal_sum(n):
    if n == 0:
        return 0
    return cal_sum(n-1) + n     # Adding n, calculates the sum of n natural numbers.

sum1 = cal_sum(5)
sum2 = cal_sum(10)
print(sum1, sum2)


#  Write a recursive function to print all elements in a list.
#  Hint: use list and index as parameters.

def print_list(list, idx=0):
    if idx == len(list):
        return 
    print(list[idx])
    print_list(fruits, idx+1)

fruits = ["mango", "pineapple", "Litchi", "Banana"]
print_list(fruits)