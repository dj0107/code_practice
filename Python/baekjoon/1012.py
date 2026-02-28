import sys
input = sys.stdin.readline

def DFS(x, y):
    """ 1인 칸에서부터 시작해 상하좌우로 재귀적으로 호출하며 1을 0으로 바꿔버림."""
    farm[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < w and 0 <= ny < h and farm[nx][ny] == 1:
            DFS(nx, ny)

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
t = int(input())
for _ in range(t):
    w, h, k = map(int, input().split())
    farm = [[0] * h for _ in range(w)] #farm[x][y]
    for __ in range(k):
        x, y = map(int, input().split())
        farm[x][y] = 1
    worm = 0
    for i in range(w):
        for j in range(h):
            if farm[i][j] == 1:
                worm += 1
                DFS(i, j)
    
    print(worm)