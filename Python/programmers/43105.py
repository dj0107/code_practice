def solution(triangle):
    answer = 0

    
    height = len(triangle)
    dp = [[] for i in range(height)]

    dp[0].append(triangle[0][0])
    for i in range(1, height):
        for j in range(0, i+1):
            if j == 0:
                dp[i].append(dp[i-1][0] + triangle[i][0])
            elif j == i:
                dp[i].append(dp[i-1][j-1] + triangle[i][j])
            else:
                dp[i].append(triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j]))
    
    answer = dp[height-1][0]
    for i in range(height-1):
        answer = max(answer, dp[height-1][i+1])

    return answer