from collections import deque
m, n = map(int, input().split()) #nxm 배열로 하기

box = []
q = deque()
for i in range(n):
    box.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if box[i][j] == 1: q.append((i, j, 0))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
maxdate = 0
while q:
    x, y, t = q.popleft()
    maxdate = max(maxdate, t)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < n) and (0 <= ny < m) and box[nx][ny] == 0:
            box[nx][ny] = 1
            q.append((nx, ny, t+1))

fail = False

for i in range(n):
    for j in range(m):
        if box[i][j] == 0: fail = True

if fail:
    print(-1)
else:
    print(maxdate)