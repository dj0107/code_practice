import sys
from collections import deque

input = sys.stdin.readline

def bfs(maze):
    q = deque()
    n = len(maze)
    m = len(maze[0])
    x = 0
    y = 0
    level = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    maze[0][0] = -1
    q.append([0, 0, 1])
    while q:
        p = q.popleft()
        x = p[0]
        y = p[1]
        level = p[2]
        maze[x][y] = -1
        # print(f"visited {x}, {y}")
        if x == n - 1 and y == m - 1:
            return level
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx <= n - 1) and (0 <= ny <= m - 1) and maze[nx][ny] == 1:
                q.append([nx, ny, level + 1])
                # print(f"appended {nx}, {ny}")




n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

print(bfs(maze))
