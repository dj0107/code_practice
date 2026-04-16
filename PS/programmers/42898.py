def solution(m, n, puddles):
    answer = 0
    dp = [[1] * m for _ in range(n)]
    for puddle in puddles:
        dp[puddle[1] - 1][puddle[0] - 1] = 0
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                dp[i][j] = 1
            elif i == 0:
                if dp[i][j] != 0:
                    dp[i][j] = dp[i][j-1]
            elif j == 0:
                if dp[i][j] != 0:
                    dp[i][j] = dp[i-1][j]
            else:
                if dp[i][j] != 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[n-1][m-1] % 1000000007

