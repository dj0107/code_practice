import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
std = [i for i in range(n+1)]
graph = [{} for _ in range(n+1)]
degin = [0] * (n+1)
q = deque()

for _ in range(m):
    s1, s2 = map(int, input().split())
    graph[s1][s2] = 1
    degin[s2] += 1
for i in range(1, n+1):
    if degin[i] == 0:
        q.append(i)

ans = []
while q:
    curr = q.popleft()
    ans.append(curr)
    for next in graph[curr]:
        degin[next] -= 1
        if degin[next] == 0: q.append(next)

print(*ans)