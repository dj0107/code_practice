import sys
from collections import deque
input = sys.stdin.readline

def DFS(idx, visited):
    Cycle = False
    global graph, n
    for i in range(n):
        if graph[idx][i] == 1 and i not in visited:
            # 다시 확인하기 싫으니까 그 간선 그냥 날리기
            graph[idx][i] = 0
            graph[i][idx] = 0 # 혹시 몰라서 반대방향도 제거(어차피 comp로 데크에서 빼버리긴 할거임)
            visited.append(i)
            if DFS(i, visited) == True:
                Cycle = True
        elif  graph[idx][i] == 1 and i in visited:
            # 사이클 감지된 경우.
            Cycle = True
    
    return Cycle




cnt = 0
while True:
    cnt += 1
    n, m = map(int, input().split())
    if n == m == 0: break
    nodes = deque()
    graph = [[0] * n for _ in range(n)] # 자기 자신으로는 가기 싫으니까 그냥 0 해놓기
    treeNum = 0
    for i in range(m):
        v1, v2 = map(int, input().split())
        graph[v1-1][v2-1], graph[v2-1][v1-1] = 1, 1
    for i in range(n): nodes.append(i)

    while nodes:
        visited = []
        node = nodes.popleft()
        visited.append(node)
        Cycle = DFS(node, visited)
        # comps들은 nodes에서 제거
        for i in visited:
            if i in nodes: nodes.remove(i)

        if not Cycle: treeNum += 1
    
    if treeNum == 0: print(f"Case {cnt}: No trees.")
    elif treeNum == 1: print(f"Case {cnt}: There is one tree.")
    else: print(f"Case {cnt}: A forest of {treeNum} trees.")






    

