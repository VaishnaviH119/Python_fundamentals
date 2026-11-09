n = int(input())
arr = list(map(int, input().split()))
avg = sum(arr) / n
count = 0
for x in arr:
    if x > avg:       
        count += 1
print(count)
