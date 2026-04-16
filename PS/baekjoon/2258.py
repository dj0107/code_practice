import sys
input = sys.stdin.readline

n, req = map(int, input().split())
meats = []
for _ in range(n):
    w, c = map(int, input().split())
    meats.append((c, w))

meats.sort(key=lambda x: (x[0], -x[1]))  # (가격, -무게)

sum = 0
tmpSum = 0 # 같은 가격일때 저장용
sameNum = 0
bestPrice = float('inf')
for i in range(n):
    cost = meats[i][0]
    if i > 0 and cost == meats[i-1][0]:
        tmpSum += meats[i-1][1]
        sameNum += 1
    elif i > 0:
        sum += tmpSum + meats[i-1][1]
        tmpSum = 0
        sameNum = 0

    if meats[i][1] + sum >= req:
        bestPrice = min(bestPrice, meats[i][0])
    elif meats[i][1] + tmpSum + sum >= req:
        bestPrice = min(bestPrice, (sameNum + 1) * meats[i][0])


if bestPrice == float('inf'): print(-1)
else: print(bestPrice)