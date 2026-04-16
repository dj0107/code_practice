n = int(input())
arr = list(map(int, input().split()))
arr.sort()
cumSum, sum = 0, 0
for time in arr:
    sum += time
    cumSum += sum
print(cumSum)