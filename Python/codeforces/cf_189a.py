n, a, b, c = map(int, input().split())
dp = [-9999] * (n+1)
dp[0] = 0
for i in range(1, n+1):
    dpa = -9999
    dpb = -9999
    dpc = -9999
    if i >= a:
        dpa = dp[i - a] + 1
    if i >= b:
        dpb = dp[i - b] + 1
    if i >= c:
        dpc = dp[i - c] + 1
    
    dp[i] = max(dpa, dpb, dpc)
    # print(f"dp[{i}]: {dp[i]}")

print(dp[n])