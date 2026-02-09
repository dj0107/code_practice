n = int(input())
dp = [0] * 10 # 0~9
dpp = [0] * 10

for i in range(1, 10): dp[i] = 1
while n > 1:
    n -= 1

    for i in range(10):
        if i == 0: dpp[1] += dp[i]
        elif i == 9: dpp[8] += dp[i]
        else:
            dpp[i+1] += dp[i]
            dpp[i-1] += dp[i]
    dp = dpp[:]
    dpp = [0] * 10

print(sum(dp) % 1000000000)