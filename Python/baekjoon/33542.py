import sys
input = sys.stdin.readline

goal, curr = map(int, input().split())# 목표, 현재
n = int(input())
INF = float('inf')

left, right = [], []

for i in range(1, n+1):
    l, r = map(int, input().split())
    left.append((l, i))
    right.append((r, i))

left.sort()
right.sort()

if curr > goal:
    print(-1, -1)
ideal = goal - curr + 1
onehand = False
for i in range(n):
    if left[i][0] == ideal and not onehand:
        onehand = True
        print(left[i][1], -1)

for i in range(n):
    if right[i][0] == ideal and not onehand:
        onehand = True
        print(-1, right[i][1])

if not onehand:
    bestl, bestr = 0, 0
    mostClose = INF
    for l in left:
        fail = False
        req = goal - curr - l[0]
        start = 0
        end = n - 1
        while start < end:
            mid = (start + end) // 2
            if right[mid][0] > req:
                end = mid - 1
            elif right[mid][0] < req:
                start = mid + 1
            else:
                break
        if mid > 0: mid -= 1
        cnt = 0
        while not (right[mid][0] > req and right[mid][1] != l[1]):
            mid += 1
            cnt += 1
            if mid == n or cnt == 3: 
                fail = True
                break
        if not fail and curr + l[0] + right[mid][0] < mostClose:
            mostClose = curr + l[0] + right[mid][0]
            bestl, bestr = l[1], right[mid][1]

    if mostClose == INF:
        print("No")
    else:
        print(bestl, bestr)
