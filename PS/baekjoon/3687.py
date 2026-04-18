t = int(input())

for _ in range(t):
    n = int(input())
    myMax, myMin = 0, ''
    # 큰 수 구하기
    
    num1 = n // 2 if n % 2 == 0 else (n-3) // 2 
    myMax = int('7' * (n % 2) + '1' * num1)
    # print(myMax)

    # 작은 수 구하기
    leng = (n-1) // 7 + 1 # 자릿수

    for i in range(1, leng+1):
        remains = leng - i
        # 0으로 채울 수 있는지 확인
        if i != 1 and remains * 2 <= n-6 <= remains * 7:
            myMin += '0'
            n -= 6
        elif remains * 2 <= n-2 <= remains * 7: # 1 되는지 확인
            myMin += '1'
            n -= 2
        elif remains * 2 <= n-5 <= remains * 7: # 2 되는지 확인
            myMin += '2'
            n -= 5
        elif remains * 2 <= n-4 <= remains * 7: # 4 되는지 확인
            myMin += '4'
            n -= 4
        elif remains * 2 <= n-6 <= remains * 7: # 6 되는지 확인
            myMin += '6'
            n -= 6
        elif remains * 2 <= n-3 <= remains * 7: # 7 되는지 확인
            myMin += '7'
            n -= 3
        elif remains * 2 <= n-7 <= remains * 7: # 8 되는지 확인
            myMin += '8'
            n -= 7
        
    
    myMin = int(myMin)
    print(myMin, myMax)