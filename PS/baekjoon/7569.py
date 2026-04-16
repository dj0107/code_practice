import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())

box = [[] for _ in range(h)] #층->세로->가로 구조
for i in range(h):
    for j in range(n):
        box[i].append(list(map(int, input().split())))

q = deque() # (i, j, k, day)

# visited = [[[False] * m for _ in range(n)] for _ in range(h)]
# print("층:", len(visited))
# print("세로:", len(visited[0]))
# print("가로:", len(visited[0][0]))
# print(box)

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1: 
                q.append((i, j, k, 0))
                # visited[i][j][k] = True

dx, dy, dz = [0, 0, 1, -1, 0, 0], [1, -1, 0, 0, 0, 0], [0, 0, 0, 0, 1, -1]
day = -1
while q:
    x, y, z, day = q.popleft()
    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        if (0 <= nx < h and 0 <= ny < n and 0 <= nz < m) and\
             box[nx][ny][nz] == 0:
            box[nx][ny][nz] = 1
            q.append((nx, ny, nz, day + 1))

left = False
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0: left = True

if left: print(-1)
else: print(day)