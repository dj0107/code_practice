import sys
input = sys.stdin.readline
INF = float('inf')
n, k = map(int, input().split())
things = []
for i in range(n):
    w, v = map(int, input().split())
    things.append([w, v]) # [무게, 가치]

dp = [[0] * (k+1) for _ in range(n+1)] # 개수 x 무게
for i in range(1, n+1):
    for j in range(1, k+1):
        if things[i-1][0] > j: # 지금 추가로 고려할 수 있게된 물건이 현재의 총가용무게를 넘어서 고려할 필요도 없는 경우, 이전 경우와 동일
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-things[i-1][0]] + things[i-1][1])

print(dp[n][k])
