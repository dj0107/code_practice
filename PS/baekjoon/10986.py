n, m = map(int, input().split())
origin = list(map(int, input().split()))

cumulative = [origin[0]]
for i in range(1, n):
    cumulative.append(cumulative[i-1] + origin[i])

# maxstep = (cumulative[-1] // m) + 1

# steps = [[0 for _ in range(maxstep)] for _ in range(m)]

totals = [0] * m
for e in cumulative:
    totals[e % m] += 1

total = 0

for i in range(len(totals)):
    if i == 0:
        total += totals[i] * (totals[i]+1) // 2
    else:
        total += totals[i] * (totals[i]-1) // 2

print(total)

# for e in cumulative:
#     steps[e % m][e // m] += 1

# for i in range(steps):
#     for j in range(steps[0]):
#         if steps[]