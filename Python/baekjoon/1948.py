import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [{} for _ in range(n+1)]
rgraph = [{} for _ in range(n+1)]
for _ in range(m):
    src, dst, w = map(int, input().split())
    graph[src][dst] = w
    rgraph[dst][src] = w

han, rome = map(int, input().split())

# han에서부터 BFS
q = deque() #(위치, 총시간)
city_max = [0] * (n+1)
q.append((han, 0))
while q:
    curr, time = q.popleft()
    if time != city_max[curr]: continue # 다른 데서 더 나은(오래걸리는) 경로가 추가된거니 스킵

    for next in graph[curr]:
        if time + graph[curr][next] > city_max[next]: # 같은 도시에 갔는데 시간을 절약했다면 그건 버림
            city_max[next] = time + graph[curr][next]
            q.append((next, city_max[next]))



print(city_max[rome])

graph = []
maxtime = city_max[rome]
# 또다시 BFS
golden = [{} for _ in range(n+1)]
# han에서부터 BFS
q = deque() #(위치, 총시간)
visited = [False] * (n+1)

for i in range(n+1):
    city_max[i] = maxtime - city_max[i]
q.append((rome, 0))
while q:
    curr, time = q.popleft()
    if visited[curr]: continue
    visited[curr] = True

    for next in rgraph[curr]:
        if time + rgraph[curr][next] == city_max[next]:
            golden[curr][next] = 1
            q.append((next, city_max[next]))



numgold = 0
for i in range(n+1):
    numgold += len(golden[i])

print(numgold)

            



