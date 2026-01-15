from collections import deque
def solution(maps):
    answer = 0
    x = y = 0
    level = 1
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    # visit (0,0)
    q.append((0, 0, level))
    maps[0][0] = 0
    while q:
        x, y, level = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m) and maps[nx][ny] == 1:
                q.append((nx, ny, level+1))
                maps[nx][ny] = 0
                if nx == n-1 and ny == m-1:
                    return level + 1

    
    return -1