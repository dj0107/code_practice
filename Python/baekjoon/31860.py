nmk = list(map(int, input().split()))
N = nmk[0]
M = nmk[1]
K = nmk[2]

D = []
day = 0
for i in range(0, N):
    D.append(int(input()))
    day += (D[i] - K) // M
    if((D[i] - K) % M) != 0: day += 1
print(day)

happy = 0
for i in range(day):
    cur = D.index(max(D))
    happy = (happy // 2) + (D[cur])
    D[cur] -= M
    print(happy)