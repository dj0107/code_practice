import sys
input = sys.stdin.readline
def getArea(x1, x2, x3, y1, y2, y3):
    return abs(x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3) / 2

n = int(input())
areaSum = 0
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

for i in range(n-2):
    areaSum += getArea(points[i][0], points[i+1][0],\
                        points[i+2][0], points[i][1], \
                            points[i+1][1], points[i+2][1])

print(round(areaSum, 1))