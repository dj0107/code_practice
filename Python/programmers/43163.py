from collections import deque
def solution(begin, target, words):
    answer = 0
    n = len(words)
    nlist = [[] for i in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if isNeighbor(words[i], words[j]):
                nlist[i].append(j)
                nlist[j].append(i)
    # step 1: startpoint
    level = 1
    q = deque()
    visited = [False] * n
    for i in range(n):
        if isNeighbor(begin, words[i]):
            q.append((i, level))
            visited[i] = True
            if words[i] == target:
                return 1
    if not q: return 0
    # step 2: iteration
    while q:
        current, level = q.popleft()
        for idx in nlist[current]:
            if not visited[idx]:
                q.append((idx, level+1))
                visited[idx] = True
                if words[idx] == target:
                    return level+1

    return 0
def isNeighbor(x, y):
    n = len(x)
    cnt = 0
    for i in range(n):
        if x[i] != y[i]: cnt += 1
    if cnt == 1: return True
    return False

