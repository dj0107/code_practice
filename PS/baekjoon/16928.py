from collections import deque

n, m = map(int, input().split())
ladder, snake = {}, {}
for _ in range(n):
    src, dst = map(int, input().split())
    ladder[src] = dst

for _ in range(m):
    src, dst = map(int, input().split())
    snake[src] = dst

q = deque()
q.append((1, 0))
visited = [False] * 101
run = True
while q and run:
    curr, level = q.popleft()
    for i in range(1, 7):
        next = curr + i
        if next in ladder: next = ladder[next]
        if next in snake: next = snake[next]

        if next < 100 and not visited[next]: 
            q.append((next, level + 1))
            visited[next] = True
        elif next == 100:
            print(level + 1)
            run = False
            break

