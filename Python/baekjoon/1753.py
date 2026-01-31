import sys
import heapq
INF = float('inf')
input = sys.stdin.readline
v, e = map(int, input().split())
edges = [{} for _ in range(v + 1)]

s = int(input())
for i in range (e):
    start, end, weight = map(int, input().split())
    if end in edges[start]:
        if weight < edges[start][end]: edges[start][end] = weight
    else: edges[start][end] = weight 

# 다익스트라 시작
D = [INF] * (v+1)
D[s] = 0
# for i in range(1, v+1): pq.put((D[i], i))
pq = [(0, s)]

while pq:
    dist, vertice = heapq.heappop(pq)
    if dist == INF: break
    for dst in edges[vertice].keys():
        if D[dst] > edges[vertice][dst] + D[vertice]:
            D[dst] = edges[vertice][dst] + D[vertice]
            heapq.heappush(pq, (edges[vertice][dst] + D[vertice], dst))

for i in range(1, v+1):
    if D[i] == INF: print('INF')
    else: print(D[i])


    



