a = input()
b = input()
na = len(a)
nb = len(b)

dp = [[0] * na for _ in range(nb)]

for i in range(nb):
    for j in range(na):
        matched = 1 if a[j] == b[i] else 0
        dp[i][j] = matched
        if i > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j] + matched)
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i][j-1] + matched)
        
        dp[i][j] = min(dp[i][j], i+1, j+1)


print(dp[nb-1][na-1])

