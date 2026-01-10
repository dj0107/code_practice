t = int(input())
for i in range(t):
    n, m, x = map(int, input().split()) # n: 사람수 m: 시행수 x: 첫 사람 번호(1~n)->일단 0~n-1로 두고 출력할때 +1하기
    r = [] # 넘길 칸수
    c = [] # 방향. 0: 시계 1: 반시계 ?:랜덤
    for j in range(m):
        temp = input().split()
        r.append(int(temp[0]))
        c.append(temp[1])
    
    grid = [[0] * n for _ in range(m+1)] #세로길이 m, 가로길이 n의 행렬. 0이면 공 없음, 1이면 가질 수 있음
    grid[0][x-1] = 1 # 최초 시작점
    for j in range(m):
        for k in range(n): # 지금의 가로행을 읽고 1을 찾아 r 연산 하여 다음 행에 저장
            if grid[j][k] == 1 and c[j] == '0':
                target = k + r[j] if k + r[j] < n else k + r[j] - n
                grid[j+1][target] = 1
            elif grid[j][k] == 1 and c[j] == '1':
                target = k - r[j] if k - r[j] >= 0 else k - r[j] + n
                grid[j+1][target] = 1
            elif grid[j][k] == 1 and c[j] == '?':
                target = k + r[j] if k + r[j] < n else k + r[j] - n
                grid[j+1][target] = 1

                target = k - r[j] if k - r[j] >= 0 else k - r[j] + n
                grid[j+1][target] = 1
            
        #print(grid[j])        
    
    final_res = []
    for j in range(n):
        if grid[m][j] == 1:
            final_res.append(j + 1)

    print(len(final_res))
    print(*final_res)
    