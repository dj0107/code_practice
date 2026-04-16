import heapq
import sys
input = sys.stdin.readline
INF = float('inf')
n, m, k = map(int, input().split()) # 정점, 간선, 교체주기
graph = [{} for _ in range(n+1)]
for _ in range(m):
    v1, v2, w = map(int, input().split()) # 정점1, 정점2, 시간
    graph[v1][v2], graph[v2][v1] = w, w

x = int(input())
exits = list(map(int, input().split()))

# 1. 다익스트라로 각 정점 가는 최단거리 구하기
D = [INF] * (n+1) # 0번 정점은 없음
D[1] = 0
pq = [(0, 1)]# 첫 정점인 1만 넣기
while pq:
    t, vertex = heapq.heappop(pq)
    if t != D[vertex]: continue
    for target in graph[vertex].keys(): # 현재 정점의 이웃들에 대해서
        if D[target] > D[vertex] + graph[vertex][target]:
            D[target] = D[vertex] + graph[vertex][target]
            heapq.heappush(pq, (D[target], target))

# 2. 각 출구에 대해서 최단시간 찾기. 
# 출구 도달 시 안열려있으면 거기서 열리는시간까지 기다림
for i in range(x):
    exitTime = D[exits[i]]
    # print(exitTime)
    cycle = (exitTime // k) % x
    # print(f"cylce: {cycle}")
    opencycle = i # 열리는 주기
    
    if cycle != opencycle: # 시간이 안맞는 경우 다음 주기까지 기다리기
        # print("wait")
        reqstep = opencycle - cycle if opencycle > cycle else x + opencycle - cycle
        exits[i] = exitTime + (reqstep * k) - (exitTime % k)
        # print(exits[i])
    else:
        exits[i] = D[exits[i]]

print(min(exits))


