def check(a, b):
    if a - b <= 1 and a - b >= -1:
        return True
    else:
        return False

n = int(input())
boys = sorted(map(int, input().split()))
m = int(input())
girls = sorted(map(int, input().split()))



dp = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        
        dp[i][j] = 1 if check(boys[i], girls[j]) else 0
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i][j-1])
        if i > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j])
        if i > 0 and j > 0 and check(boys[i], girls[j]):
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)

print(dp[n-1][m-1])