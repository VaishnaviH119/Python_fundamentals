# 6. Write a program to check whether a given number is prime. 

# prime logic
# multiple -> 1 and number itself

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter any number: "))
prime = is_prime(n)
print(prime)


# start from 3, handle 2 separately as an edge case and the factors of 2 are composites
# and handle them as well in another case. 
# Loop from 3 to sqrt of the number and +1 to get the last excluded number as well, and 
# 2 is the step size to check for odd numbers and composites only
# if the number is odd and prime it will be not give remainder as 0, hence the o/p will be True.
# otherwise it would be False.

def is_prime(num):
    if num < 2:
        return False                                        # 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
    if num == 2:                                             #  ----------------------------------------------
        return True                                           #  3 5 7 9 11 13 15 17 19
    if num % 2 == 0:
        return False
    
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i != 0:
            return True
    return False

