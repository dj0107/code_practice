from collections import deque
n, m = map(int, input().split())
maze = [[0]* m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
for i in range(n):
    st = input()
    for j in range(m):
        maze[i][j] = int(st[j])
q = deque()
q.append((0, 0, 0, 1))
visited = [[[False] * m for _ in range(n)] for _ in range(2)]
# visited[1]은 벽을 부순 경우, [0]은 아직 안부순 경우
visited[0][0][0] = True
visited[1][0][0] = True
answer = 999999999
while q:
    x, y, bNum, level = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < n) and (0 <= ny < m) and not visited[bNum][nx][ny]:
            if maze[nx][ny] == 1 and bNum == 0: 
                # 벽 하나 무시
                q.append((nx, ny, 1, level+1))
                visited[1][nx][ny] = True
            elif maze[nx][ny] == 0: # 벽이 없음
                q.append((nx, ny, bNum, level+1))
                visited[bNum][nx][ny] = True
            # 나머지 경우(벽이 있는데 이미 벽을 부숨)는 진행 x
            if nx == n-1 and ny == m-1:
                answer = min(answer, level+1)
if n == m == 1:
    print(1)
elif answer == 999999999:
    print(-1)
else:
    print(answer)
