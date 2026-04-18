import sys
import heapq
input = sys.stdin.readline
n = int(input())
arr = []
sum = 0
for i in range(n):
    heapq.heappush(arr, int(input()))

for i in range(n-1):
    left = heapq.heappop(arr)
    right = heapq.heappop(arr)
    sum += left + right
    heapq.heappush(arr, left + right)

print(sum)


