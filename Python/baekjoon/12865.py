import sys
input = sys.stdin.readline
n, k = map(int, input().split())
things = []
for i in range(n):
    w, v = map(int, input().split())
    things.append([w, v])

things.sort() # 이게 필요할까 굳이?
dp = [[0, 0]] * n # 지금은 0 이지만 나중에 (총무게, 총가치)로 바뀜
dp[0] = [things[0][0], things[0][1]] if things[0][0] <= k else [0, 0]
for i in range(1, n):
    for j in range(i):
        if dp[j][0] + things[i][0] <= k and (dp[i][1] < dp[j][1] + things[i][1] or (dp[j][0] + things[i][0] < dp[i][1] and dp[i][1] == dp[j][1] + things[i][1])):
            dp[i][1] = dp[j][1] + things[i][1]
            dp[i][0] = dp[j][0] + things[i][0]
ans = 0
for i in range(n):
    ans = max(ans, dp[i][1])
print(ans)
            
