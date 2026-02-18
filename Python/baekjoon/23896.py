# google kickstart 2020 A - Plates
t = int(input())
for tt in range(1, t+1):
    n, k, p = map(int, input().split())
    plates = [] 
    for i in range(n):
        plates.append(list(map(int, input().split())))
    
    # plates는 n x k의 2차원 배열

    dp = [[0] * (n+1) for _ in range(p+1)] #[총 개수]][플레이트 사용할 범위]
    for i in range(1, p+1): # i개만큼 접시를 고르는 거임.
        for j in range(1, n+1): # j+1번째 스택까지를 사용하는 거임.
            # print(i, j)
            cnt = curmax = 0
            while True:
                if i-cnt < 0 or cnt > k or cnt > p: break
                curmax = max(curmax, dp[i-cnt][j-1] + sum(plates[j-1][:cnt]))
                cnt += 1
            
            dp[i][j] = curmax

    print(f"Case #{tt}: {dp[p][n]}")

