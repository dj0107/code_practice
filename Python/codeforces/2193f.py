import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):

    n, Ax, Ay, Bx, By = map(int, input().split())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    pizza = []
    for i in range(n):
        pizza.append((xs[i], ys[i]))
    # x에 대해서 sort
    pizza.sort()
    xs = list(set(xs))
    # print(pizza)
    # print(xs)
    dist = Bx - Ax
    cnt = 0
    cur_y = Ay
    greedyu, greedyd = 0, 0
    for x in xs:
        ypoints = []
        while pizza[cnt][0] == x:
            ypoints.append(pizza[cnt][1])
            cnt += 1
        upMostY = ypoints[-1]
        downMostY = ypoints[0]
        greedyu = max(greedyu + abs(cur_y))