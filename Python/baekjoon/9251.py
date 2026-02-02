a = input()
b = input()
na = len(a)
nb = len(b)

dp = [[0] * (na+1) for _ in range(nb+1)]

for i in range(1, nb+1):
    for j in range(1, na+1):
        if a[j-1] == b[i-1]:
            dp[i][j] = max(dp[i-1][j-1] + 1, dp[i-1][j], dp[i][j-1])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[nb][na])

