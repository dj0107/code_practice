import heapq
import sys
input = sys.stdin.readline
INF = float('inf')
n = int(input())
m = int(input())
buses = [{} for i in range(n+1)]
for _ in range(m):
    start, end, weight = map(int, input().split())
    buses[start][end] = min(buses[start].get(end, 100001), weight)

s, e = map(int, input().split())
# 다익스트라
D = [INF] * (n+1)
D[s] = 0
hq = [(0, s)]# (비용, 지점)
while hq:
    cost, point = heapq.heappop(hq)
    for dst in buses[point].keys():
        if D[dst] > D[point] + buses[point][dst]:
            D[dst] = D[point] + buses[point][dst]
            heapq.heappush(hq, (D[dst], dst))

print(D[e])