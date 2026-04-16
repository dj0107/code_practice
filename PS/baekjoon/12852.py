n = int(input())

INF = float('inf')
dp = [INF] * (n+1)

dp[1] = 0
if n > 1: dp[2] = 1
for i in range(3, n+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0: dp[i] = min(dp[i//3] + 1, dp[i])
    if i % 2 == 0: dp[i] = min(dp[i//2] + 1, dp[i])

cur = n
route = [n]
while cur > 1:
    best = cur - 1
    if cur % 2 == 0 and dp[cur // 2] < dp[best]: best = cur // 2
    if cur % 3 == 0 and dp[cur // 3] < dp[best]: best = cur // 3
    route.append(best)
    cur = best

print(dp[n])
print(*route)
