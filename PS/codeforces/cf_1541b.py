import sys
t = int(input())
for k in range(t):
    n = int(input())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    arr.insert(0, 0)
    cnt = 0
    for i in range(1, n + 1):
        for j in range(arr[i] - i, n + 1, arr[i]):
            if j > i and arr[i] * arr[j] == i + j:
                cnt += 1

    print(cnt)
