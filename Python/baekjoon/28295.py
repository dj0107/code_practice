# Created on iPad.

deg = 0

for _ in range(10):
    T = int(input())
    deg += T * 90

deg = deg % 360
if deg == 0: print('N')
elif deg == 90: print('E')
elif deg == 180: print('S')
elif deg == 270: print('W')