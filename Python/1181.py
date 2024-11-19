# Created on 신동주의 iPad.

N = int(input())
arr = []
for i in range(0,N):
    arr.append(input())

arr.sort()
ans = []
for i in range(1,51):
    for j in range(0, N):
        if len(arr[j]) == i:
            ans.append(arr[j])

max = N - 1
counter = 0

while counter < max:
    if ans[counter] == ans[counter + 1]:
        del ans[counter]
        max -= 1
    else: counter+= 1

for i in range(0,max + 1):
    print(ans[i])