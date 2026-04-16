import sys
from collections import deque
input = sys.stdin.readline
# n, k, m = map(int, input().split())
# graph = [{} for _ in range(n+1)]
# for _ in range(m):
#     line = list(map(int, input().split()))
#     for i in range(k):
#         for j in range(i+1, k):
#             graph[line[i]][line[j]], graph[line[j]][line[i]] = 1, 1


# q = deque()
# cnts = [n+1] * (n+1)
# cnts[1] = 1
# q.append((1, 1))
# ans = -1
# while q:
#     curr, level = q.popleft()
#     if level > cnts[curr]: continue
#     for next in graph[curr]:
#         if next == n:
#             ans = level
#             break
#         if level + 1 < cnts[next]:
#             q.append((next, level+1))
#             cnts[next] = level+1

# print(ans)

n, k, m = map(int, input().split())
cnts = [100001] * (n+1)
tubes = []
elements = [[] for _ in range(n+1)]
for i in range(m):
    line = list(map(int, input().split()))
    line.sort()
    tubes.append(line)
    for e in line:
        elements[e].append(i)

q = deque()
q.append((1,1))
visited = [False] * (n+1)
visited[1] = True
while q:
    curr, level = q.popleft()
    if level > cnts[curr]: continue
    for rowNum in elements[curr]:
        for next in tubes[rowNum]:
            if cnts[next] > level + 1 and next != curr and not visited[next]:
                q.append((next, level + 1))
                cnts[next] = level + 1
                visited[next] = True

ans = -1 if cnts[-1] == 100001 else cnts[-1]
print(ans)