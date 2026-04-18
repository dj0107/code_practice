import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [{} for _ in range(n+1)]
q = []
inarr = [0] * (n+1)
for _ in range(m):
    before, after = map(int, input().split())
    graph[before][after] = 1
    inarr[after] += 1

for i in range(1, n+1):
    if inarr[i] == 0: heapq.heappush(q, i)
ans = []
while q:
    idx = heapq.heappop(q)
    ans.append(idx)
    for nxt in graph[idx]: 
        inarr[nxt] -= 1
        if inarr[nxt] == 0:
            heapq.heappush(q, nxt)


print(*ans)