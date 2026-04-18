

while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0: break
    """
    N <= 10억
    9x1 + 90x2 + 900x3 + 9000x4 + 90000x5 + 900000x6 + 9000000x7
    """
    
    cum = [1, 10, 190, 2890, 38890, 488890, 5888890, 68888890, 788888890]
    idx = 0
    for i in range(9):
        if n >= cum[i]:
            idx = i
    # idx+1 자리인 것... 
    # 시작 숫자를 찾고, 그 시작숫자의 어디서부터 시작할지 보기...
    start = 10 ** idx
    probe = (n - cum[idx]) // (idx+1)
    remainder = (n - cum[idx]) % (idx+1) 
    start += probe
    nums = ''
    for i in range(100):
        nums += str(start + i)
    # print(nums)
    print(nums[remainder:remainder + k])



    


    
    

