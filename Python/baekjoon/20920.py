import sys
input = sys.stdin.readline
n, m = map(int, input().split())

dic = {} 
arr = []

for i in range(n):
    word = input().rstrip()
    if len(word) < m: continue
    if word in dic:
        arr[dic[word]][1] += -1
    else: # first time
        dic[word] = len(arr)
        arr.append([word, -1])

arr.sort(key=lambda x: (x[1], -len(x[0]), x[0]))
for i in range(len(arr)):
    print(arr[i][0])