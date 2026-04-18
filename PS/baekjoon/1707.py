import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit = 999999

def bfs(node, g):
    q = deque([node])
    sides[node] = g
    while q:
        next = q.popleft()
        
    
    

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = [{} for _ in range(v+1) ] # graph[0]은 고려x, 방향없음
    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1][v2], graph[v2][v1] = 1, 1
    
    sides = [0] * (v+1) # 각 노드가 속할 집합. 1/2

    for i in range(1, v+1):
        if sides[i] != 0: continue
        bfs(i, 1)
        

