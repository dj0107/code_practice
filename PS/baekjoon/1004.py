t = int(input())

for _ in range(t):
	x1, y1, x2, y2 = map(int, input().split())

	n = int(input())
	num = 0
	for _ in range(n):
		do_plus = 0
		cx, cy, r = map(int, input().split())

		if (cx-x1)** 2 + (cy-y1)**2 < r**2: do_plus = (do_plus + 1) % 2
		if (cx-x2)** 2 + (cy-y2)**2 < r**2: do_plus = (do_plus + 1) % 2

		num += do_plus
	
	print(num)