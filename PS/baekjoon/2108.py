import sys, math
input = sys.stdin.readline

n = int(input())
arr = [0] * (n+1)
for i in range(n):
    arr[i] = int(input())

#1
mean = round(sum(arr) / n)

#2
arr.sort()


