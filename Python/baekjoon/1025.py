import math

def check(n):
    return math.ceil(math.sqrt(n)) == math.sqrt(n)

answer = -1
n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, list(input()))))

for i in range(n):
    for j in range(m):
        # 각 칸에 대해서
        curnum = board[i][j]
        if check(curnum): answer = max(answer, curnum)


        for ii in range(n):
            for jj in range(m):
                # 다른 칸(ii, jj)을 고르고
                curnum = board[i][j]

                dx, dy = ii - i, jj - j # 점프 뛸 간격
                nx, ny = i + dx, j + dy # 처음엔 (ii,jj)고 이후(dx,dy)씩 더해짐
                # if dx == 0 and dy == 0: break
                while(0 <= nx < n) and (0 <= ny < m):
                    if nx == i and ny == j: break
                    # 이제 nx, ny가 정상적으로 판에 존재.
                    # 숫자 붙이기 하고 검사하기
                    curnum = curnum * 10 + board[nx][ny]
                    if check(curnum): answer = max(answer, curnum)
                    # nx, ny 한 간격만큼 더 이동
                    nx, ny = nx + dx, ny + dy
print(answer)




