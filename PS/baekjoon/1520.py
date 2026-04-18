import heapq
m, n = map(int, input().split())

arr = []
for _ in range(m):
    arr.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(m)]
dp[0][0] = 1
visited = [[False] * n for _ in range(m)]
hq = []
hq.append((-arr[0][0], 0, 0)) # 경사도는 heappop 편하게 음수로 저장
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
while hq:
    val, x, y = heapq.heappop(hq)
    if visited[x][y]: continue
    visited[x][y] = True
    val = -val
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and val > arr[nx][ny]:
            heapq.heappush(hq, (-arr[nx][ny], nx, ny))
            dp[nx][ny] += dp[x][y]

print(dp[-1][-1])


