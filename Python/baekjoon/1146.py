n = int(input())

dp = [0] * 101

dp[1] = 1
dp[2] = 1
dp[3] = 2
end_digits = [1 ,1, 0] # 1, 2, 3 (, 4, 5, 6.....)
for i in range(4, n+1):
    # end_digits를 보고 tmp를 채우기
    tmp = []
    excludes = 0
    end_digits.append(0)
    for j in range(1, i):
        excludes += end_digits[-j]
        tmp.append(dp[i-1] - excludes)
    tmp.append(0)
    end_digits = tmp[:]
    dp[i] = sum(end_digits)
    if i % 2 == 1: end_digits.reverse()

if n == 1:
    print(1)
else:
    print(dp[n] * 2)