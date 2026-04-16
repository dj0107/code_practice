import sys, heapq
input = sys.stdin.readline

def dijkstra(src, dst):
    D = [INF] * (v+1)
    D[src] = 0
    hq = [] # 거리, idx로 우선순위큐
    for i in range(v+1): heapq.heappush(hq, (D[i], i))
    while hq:
        dist, idx = heapq.heappop(hq)
        if dist > D[idx] : continue # 더 나은 경로가 있었다면 pass
        for nxt in graph[idx]:
            if graph[idx][nxt] + dist < D[nxt]:
                D[nxt] = graph[idx][nxt] + dist
                heapq.heappush(hq, (D[nxt], nxt))

    return(D[dst])

INF = float('inf')
v, e = map(int, input().split())
graph = [{} for _ in range(v+1)]
for _ in range(e):
    v1, v2, w = map(int, input().split())
    graph[v1][v2], graph[v2][v1] = w, w

v1, v2 = map(int, input().split())
ans = 0
# case 1: v1 = 1, v2 = n: 그냥 다익스트라
if v1 == 1 and v2 == v:
    ans = dijkstra(1, v)
# case 2: v1 = 1: 1-v2에 대해 다익스트라 + v2-N에 대해 다익스트라
elif v1 == 1:
    ans = dijkstra(1, v2) + dijkstra(v2, v)
    
# case 3: v2 = n: v2가 v1으로 바뀌고 case 2랑 똑같음
elif v2 == v:
    ans = dijkstra(1, v1) + dijkstra(v1, v)
# case 4: v1 != 1, v2 != n: 1-v1-v2-n, 1-v2-v1-n 하고 최솟값
else:
    ans = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, v),\
              dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, v))

if ans == INF:
    print(-1)
else: print(ans)