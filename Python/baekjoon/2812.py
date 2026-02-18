import sys
n, k = map(int, input().split())
num = sys.stdin.readline().strip('')
# num = '123456789' + '0123456789' * 10000
to_delete = [0] * n
deleted = 0
curr = 1
# curr 포인터를 한 칸씩 앞으로 가면서 자기 이전 애가 자기보다 작은 상황이 생길 시

while deleted < k and curr < n:
    if num[curr] > num[curr-1]:
        for i in reversed(range(0, curr)):
            if num[curr] <= num[i]:
                break
            elif to_delete[i] == 0:
                to_delete[i] = 1
                deleted += 1
                if deleted == k: break
    curr += 1

# if deleted < k and num[n-1] < num[n-2]: 
#     to_delete[-1] = 1
#     deleted += 1
answer = ''.join(num[i] for i in range(n) if to_delete[i] == 0)

if deleted < k:
    extra = k - deleted
    answer = answer[:len(answer) - extra]
print(answer)

