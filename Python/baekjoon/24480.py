import sys
input = sys.stdin.readline
sys.setrecursionlimit(120000)
def DFS(start):
    """함수 실행 시점에는 start가 미방문상태임이 보장됨"""
    global visited, ans
    visited[start] = True
    ans.append(start)
    nexts = sorted(graph[start], reverse=True)
    for next in nexts:
        if not visited[next]:
            DFS(next)

n, m, r = map(int, input().split())
graph = [{} for _ in range(n+1)]
visited = [False] * (n+1)
ans = []
for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v], graph[v][u] = 1, 1

DFS(r)

order = [0] * (n+1)
for i in range(len(ans)):
    target = ans[i]
    order[target] = i + 1

for i in range(1, n+1):
    print(order[i])

