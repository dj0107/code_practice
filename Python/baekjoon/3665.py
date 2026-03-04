import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):  
    n = int(input())
    degin = [0] * (n+1)
    past = list(map(int, input().split()))
    graph = [{} for _ in range(n+1)]
    visited = [False] * (n+1)
    visited[0] = True # 0번은 없는 존재라 방문 금지
    cnt = 0
    for p in past:
        visited[p] = True
        degin[p] = cnt
        cnt += 1
        for i in range(1, n+1):
            if not visited[i]: graph[p][i] = 1
    
    m = int(input())
    for _ in range(m):
        t1, t2 = map(int, input().split())
        # 방향 전환
        if t2 in graph[t1]: # t1->t2였던 경우
            del graph[t1][t2]
            graph[t2][t1] = 1
            # degin도 바꾸기
            degin[t2] -= 1
            degin[t1] += 1
        else: # t2->t1 였던 경우
            del graph[t2][t1]
            graph[t1][t2] = 1
            degin[t1] -= 1
            degin[t2] += 1
    
    # 위상정렬

    q = deque()
    ans = []
    for i in range(1, n+1):
        if degin[i] == 0: q.append(i)
    # visited = [False] * (n+1) # 위상정렬 체크용으로 visited 다시 초기화
    while q:
        curr = q.popleft()
        ans.append(curr)
        # visited[curr] = True
        for next in graph[curr]:
            degin[next] -= 1
            if degin[next] == 0: q.append(next)
    
    if len(ans) != n:
        print("IMPOSSIBLE")
    else:
        print(*ans)

