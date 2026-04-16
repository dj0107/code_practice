import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    upper = list(map(int, input().split()))
    lower = list(map(int, input().split()))

    dp = [[0] * 3 for _ in range(n)]
    dp[0][0] = upper[0] #upper
    dp[0][1] = lower[0] #lower
    dp[0][2] = 0 # choose nothing

    for i in range(1, n):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + upper[i]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + lower[i]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
    
    print(max(dp[n-1][0], dp[n-1][1], dp[n-1][2]))