import sys
from collections import deque
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [{} for _ in range(v+1)]
odds = [0] * (v+1)
for _ in range(e):
    v1, v2 = map(int, input().split())
    graph[v1][v2], graph[v2][v1] = 1, 1
    odds[v1] = (odds[v1] + 1) % 2
    odds[v2] = (odds[v2] + 1) % 2

visited = [False] * (v+1)

subGraph = []
for i in range(1, v+1):
    if visited[i]: continue
    
    tmp = []
    q = deque()
    q.append(i)
    while q: #bfs
        cur = q.popleft()
        if visited[cur]: continue
        tmp.append(cur)
        visited[cur] = True
        for nxt in graph[cur]:
            if not visited[nxt]:
                q.append(nxt)
    
    subGraph.append(tmp)

req = len(subGraph) - 1
for sub in subGraph:
    odd_total = 0
    for comp in sub:
        odd_total += odds[comp]
    req += max((odd_total - 2) // 2, 0)

print(req)


