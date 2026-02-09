def MM(A, B):
    n = len(A)
    M = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            sum = 0
            for k in range(n):
                sum += A[i][k]*B[k][j]
            sum = sum % 1000
            M[i][j] = sum
    return M

n, b = map(int, input().split())
A = [[0] * n for _ in range(n)]
for i in range(n):
    A[i] = list(map(int, input().split()))
ndic = {}
ANS = [[0] * n for _ in range(n)]
for i in range(n): ANS[i][i] = 1
ndic[0] = A
b = bin(b)
numMax = len(b) - 3
for i in range(numMax):
    ndic[i+1] = MM(ndic[i], ndic[i])

for i in range(len(b) - 2):
    if b[len(b) - i - 1] == '1':
        ANS = MM(ANS, ndic[i])

for i in range(n):
    print(*ANS[i])
