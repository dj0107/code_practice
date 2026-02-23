n = int(input())
arr = [-1]
for _ in range(n):
    arr.append(int(input()))

dp = [0] * (n+1)
dp[1] = arr[1]
if n > 1: dp[2] = arr[1] + arr[2]
if n > 2: dp[3] = max(dp[2], arr[1] + arr[3], arr[2] + arr[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-1], arr[i] + arr[i-1] + dp[i-3], arr[i] + dp[i-2])

print(dp[-1])