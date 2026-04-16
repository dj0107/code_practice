import sys


def min_flips(x: str, y: str) -> int:
	"""Return minimal flips to make y the parity control string of x."""
	INF = 10 ** 9
	dp = [0, INF]  # dp[parity]

	for cx, cy in zip(x, y):
		ndp = [INF, INF]
		cy_val = int(cy)
		cx_val = int(cx)

		for parity in (0, 1):
			base = dp[parity]
			if base >= INF:
				continue

			# Choose bit 0 or 1 for x
			for bit in (0, 1):
				new_parity = parity ^ bit
				cost = base + (cx_val != bit) + (new_parity != cy_val)
				if cost < ndp[new_parity]:
					ndp[new_parity] = cost

		dp = ndp

	return min(dp)


def solve() -> None:
	input = sys.stdin.readline
	t = int(input().strip())
	out_lines = []

	for _ in range(t):
		x = input().strip()
		y = input().strip()
		out_lines.append(str(min_flips(x, y)))

	sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
	solve()
