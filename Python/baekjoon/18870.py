import sys
input = sys.stdin.readline
n = int(input())
pos = input().split()
arr = []
for i in range(n):
    arr.append((int(pos[i]), i))

arr.sort()
# print(arr)

ans = [0] * n
cnt = 1
prev = arr[0][0]
for i in range(1, n):
    targetIndex = arr[i][1]
    if arr[i][0] == prev:
        cnt -= 1
        ans[targetIndex] = cnt
    else:
        ans[targetIndex] = cnt
    cnt += 1
    prev = arr[i][0]

for i in range(n-1):
    print(ans[i], end=" ")
print(ans[n-1])