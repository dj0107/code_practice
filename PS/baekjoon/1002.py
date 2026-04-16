import math

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
    dist = math.sqrt(dist)
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif dist == r1 + r2 or dist + min(r1, r2) == max(r1, r2):
        print(1)
    elif dist > r1 + r2 or dist + min(r1, r2) < max(r1, r2):
        print(0)
    else: print(2)