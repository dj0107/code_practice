n = int(input())
steps = [0]
for _ in range(n):
    steps.append(int(input()))

dp = [0] * (n+1)
dp[1] = steps[1]
if n > 1: dp[2] = steps[1] + steps[2]

for i in range(3, n+1):
    dp[i] = steps[i] + max(dp[i-2], dp[i-3] + steps[i-1])

print(dp[-1])

