import sys
from bisect import bisect_left
input = sys.stdin.readline

goal, curr = map(int, input().split())# 목표, 현재
n = int(input())
INF = 99999999999

left, right = [], []

for i in range(1, n+1):
    l, r = map(int, input().split())
    left.append((l, i))
    right.append((r, i))

left.sort()
right.sort()
finish = False
if curr > goal:
    print(-1, -1)
    finish = True
ideal = goal - curr + 1
cnt = 0
while not finish and cnt < n:
    if left[cnt][0] == ideal:
        print(left[cnt][1], -1)
        finish = True
    elif right[cnt][0] == ideal:
        print(-1, right[cnt][1])
        finish = True
    cnt += 1

if not finish:
    closest = INF
    myleft = myright = 0
    
    for lval, lidx in left:
        if lval > goal - curr: break

        fail = False
        reqMin = goal - curr - lval + 1
        # 이분탐색
        idx = bisect_left(right, (reqMin, 0))
        # 찾기 실패한 경우 1: 마지막 인덱스 값을 반환
        if idx == n:
            fail = True
        # 찾기 실패한 경우 2: 마지막인데 겹침
        elif right[idx][1] == lidx:
            idx += 1
            if idx == n:
                fail = True
        
        if (not fail) and right[idx][0] + curr + lval < closest:
            closest = right[idx][0] + curr + lval
            myleft, myright = lidx, right[idx][1]

    if myleft == 0 and myright == 0:
        print("No")
    else:
        print(myleft, myright)    
