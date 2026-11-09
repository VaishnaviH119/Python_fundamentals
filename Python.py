import sys 
from colections import defalutdict, Counter
from itertools import permutations, combinations
import math

input = sys.stdin.readline  # Faster Input
print = sys.stdout.write # faster output

'''
Input Methods / Patterns 
'''

#single integer
n = int(input())
#single line of integer -> list of integers
arr = list(map(int, input().split()))
#multiple integers in one line
a, b, c = map(int, input().split())
#multiple integers in multiple lines
arr = [int(input()) for _ in range(n)]
#multiple lines of integers -> list of list of integers(2D list)
arr = [list(map(int, input().split()) for _ in range(n))]
#string input
s = input().strip() # remove trailing newline
#string input without spaces
s = input().strip().replace(" ", "")
#string input with spaces
s = input().strip()
#string input in multiple lines -> n line of strings -> list of strings
word = [input().strip() for _ in range(n)]


'''
Array / List Problems
'''
n = int(input())
arr = list(map(int, input().split()))
#sum of array
print(sum(arr))
#maximum element in array
print(max(arr))
#minimum element in array
print(min(arr))
#average of array
print(sum(arr) / len(arr))
#sort array
arr.sort()
print(arr)
#reverse array
arr.reverse()
print(arr)
#count frequency of elememt in an array
freq = Counter(arr)
print(freq)
#find unique elements in an array
unique = set(arr)
print(unique)
#find common elements in two arrays
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
common = set(arr1) & set(arr2)
print(common)
#find distinct elements in two arrays
distinct = set(arr1) ^ set(arr2)
print(distinct)
#find union of two arrays
union = set(arr1) | set(arr2)
print(union)
#find intersection of two arrays
intersection = set(arr1) & set(arr2)
print(intersection)
#find difference of two arrays
difference = set(arr1) - set(arr2)
print(difference)
#find symmetric difference of two arrays
sym_diff = set(arr1) ^ set(arr2)
print(sym_diff)
#find subarrays of an array
subarray = []
for i in range(len(arr)):
    for j in range(i, len(arr)):
        subarray.append(arr[i:j+1])
print(subarray)
#find permutations of an array 
perm = permutations(arr)
print(list(perm))
#ind combinations of an array
comb = combinations(arr, 2) # change 2 to any number for different length of combinations
print(list(comb))
#find factorial of a number
n = int(input())
print(math.factorial (n))
#find power of a number
a, b = map(int, input().split())
print(pow(a,b))
#find gcd of two numbers
import math  # imports the math module to access the gcd funvtion
a, b = map(int, input().split())
print(math.gcd()(a,b))

from math import gcd
a, b = map(int, input().split())
print(gcd(a,b))

#find lcm of two numbers
def lcm(a,b):
    return (a*b) // math.gcd(a,b)
a, b = map(int, input().split())
print(lcm(a,b))

#find prime numbers in a range
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

a, b= map(int, input().split())
primes = [i for i in range(a, b+1) if is_prime(i)]
print(primes)


#All primes up to n (Sieve of Eratosthenes)
def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return [i for i in range(2, n+1) if primes[i]]

n = int(input())
print(sieve_of_eratosthenes(n))

#find factorial of a number using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

#find factorial of a number using iteration
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

#find factorail of a number using memoization
def factorial(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    memo[n] = n * factorial(n-1, memo)
    return memo[n]

#find factorial of a number using dynamic programming
def factorial(n):
    dp = [1] * (n+1)
    for i in range(2, n+1):
        dp[i] = i * dp[i-1]
    return dp[n]

#find fibonacci series up to n terms using recursion
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n-1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

#find fibonacci series up to n terms
def fibonacci(n):
    



#Reverse a string
s = input().strip()
reversed_s = s[::-1]
print(reversed_s)

#Check if a string is a palindrome
s = input().strip()
if s == s[::-1]:
    print("Palindrome")
else:
    print("not a palindrome")

#Count frequency of characters in a string
s = input().strip()
freq = Counter(s)
print(freq)

#Prefix sum of an array
n = int(input())
arr = list(map(int, input().split()))
prefix_sum = [0] * (n+1)
for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + arr[i]
print(prefix_sum)

#Suffix sum of an array
n = int(input())
arr = list(map(int, input().split()))
suffix_sum = [0] * (n+1)
for i in range(n-1, -1, -1):
    suffix_sum[i] = suffix_sum[i+1] + arr[i]
print(suffix_sum)

#Two pointer technique to find pairs with a given sum in a sorted array
n = int(input())
arr = list(map(int, input().split()))
arr.sort() # make sure the array is sorted
target = int(input())
left, right = 0, n-1
while left < right:
    current_sum = arr[left] + arr[right]
    if current_sum == target:
        print(f"Pair found: {arr[left]}, {arr[right]}")
        left += 1
        right -= 1
    elif current_sum < target:
        left += 1
    else:
        right -= 1

#Binary search in a sorted array
def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


#Find the maximum subarray sum using Kadane's algorithm
n = int(input())
arr = list(map(int, input().split()))
max_current = max_global = arr[0]
for i in range(1, n):
    max_current = max(arr[i], max_current + arr[i])
    if max_current > max_global:
        max_global = max_current
print(max_global)

#Find the longest increasing subsequence in an array
def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

#Find the longest common subsequence between two strings
def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

#Sliding window technique to find the maximum sum of a subarray of size k
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
max_sum = 0
current_sum = sum(arr[:k])
max_sum = current_sum   
for i in range(k, n):
    current_sum += arr[i] - arr[i-k]
    max_sum = max(max_sum, current_sum)
print(max_sum)


#Frequency of elements in a sliding window of size k
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
freq = Counter(arr[:k])
print(freq)
for i in range(k, n):
    freq[arr[i]] += 1
    freq[arr[i-k]] -= 1
    if freq[arr[i-k]] == 0:
        del freq[arr[i-k]]
    print(freq)



#Find the median of a list of numbers
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
if n % 2 == 1:
    median = arr[n//2]
else:
    median = (arr[n//2 - 1] + arr[n//2]) / 2
print(median)   

#Split and join strings
s = input().strip()
words = s.split() # split string into list of words
print(words)
joined_String = " ".join(words) # join list of words into a string
print(joined_String)

#Find the length of the longest substring without repeating characters  







#Find the length of the longest substring with at most k distinct characters




#Find the length of the longest substring with at least k repeating characters





#Remove spaces / special chars from a string
s = input().strip()
cleaned_s = ''.join(e for e in s if e.isalnum()) # keep only alphanumeric characters
print(cleaned_s)