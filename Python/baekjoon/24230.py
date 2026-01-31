import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
colors = list(map(int, input().split()))
colorsNow = [0] * n
graph = [{} for _ in range(n)]
# print(graph)
for _ in range(n-1):
    v1, v2 = map(int, input().split())
    v1 -= 1 # 노드 번호 0~N-1로 수정
    v2 -= 1
    graph[v1][v2], graph[v2][v1] = 1, 1
    # 자식이 부모한테 가는 일 없게 한번 본 간선 삭제하는 기능 만들기

painted = 0
q = deque()
q.append((0,-1)) # 칠하기 명령. -1이면 없고, 1~N이면 그 색으로 칠하라는 명령이 내려온것
while q:
    now, upeffect = q.popleft()
    # 위로부터 페인트 영향이 내려온걸로 현재 컬러 바꾸기
    if upeffect != -1: colorsNow[now] = upeffect

    if colors[now] != colorsNow[now]:
        painted += 1
        colorsNow[now] = colors[now]
        upeffect = colorsNow[now] # 앞으로 자식을 upeffect로 칠하라고 명령
            
    childs = list(graph[now].keys())
    for target in childs:
        # # 이후 방문할 자식노드들 추가
        # q.append(target)
        # 자식이 부모한테 가는 일 없게 한번 본 간선 삭제하는 기능 만들기
        del graph[now][target]
        del graph[target][now]

        q.append((target, upeffect))

print(painted)

        
    
        


