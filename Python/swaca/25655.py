t = int(input())
for _ in range(t):
    x = int(input())
    
    if x == 1:
        ans = 0
    elif x % 2 == 1:
        num8 = x // 2
        ans = '4' + '8'*num8
    else:
        num8 = x // 2
        ans = '8'*num8
    print(ans)