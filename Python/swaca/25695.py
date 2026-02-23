t = int(input())
for _ in range(t):
    x, y, z = map(int, input().split())
    if (x != y and y != z and z != x) or (x == y and y < z) or (x == z and y > z) or (y == z and x > y):
        print("-1 -1 -1")
    else:
        # 다른 곳 찾기
        high = max(x, y, z)
        low = min(x, y, z)
        if x == y: print(low, high, low)
        elif x == z: print(high, low, low)
        else: print(low, low, high)
        