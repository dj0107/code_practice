t = int(input())
num = 2
prime = [True] * 1000001
prime[1] = False
prime[0] = False
while num <= 1000:
    if prime[num] == False:
        num += 1
        continue
    cnt = num * 2
    while cnt <= 1000000:
        prime[cnt] = False
        cnt += num
    num += 1

for _ in range(t):
    n = int(input())
    ans = 0
    for i in range(2, n // 2 + 1):
        if prime[i] and prime[n - i]: ans += 1
    print(ans)