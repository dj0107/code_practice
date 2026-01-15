def solution(money):
    answer = 0
    n = len(money)
    dp1 = [0] * n # do not steal 1st house
    dp2 = [0] * (n-1) # steal 1st house

    for i in range(n):
        if i == 0:
            dp1[i] = 0
        elif i == 1:
            dp1[i] = money[i]
        else:
            dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
    
    for i in range(n-1):
        if i == 0:
            dp2[i] = money[0]
        elif i == 1:
            dp2[i] = dp2[0]
        else:
            dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    
    answer = max(dp1[n-1], dp2[n-2])
    
    return answer

print(solution([1000,1,0,1,2,1000,0]))