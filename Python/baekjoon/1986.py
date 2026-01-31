n, m = map(int, input().split())
board = [[0] * m for _ in range(n)] # 0: 아직 안전 1: 말 놓임 2: 말 없지만 위험
unsafe = 0
queenarr = list(map(int, input().split()))
knightarr = list(map(int, input().split()))
pawnarr = list(map(int, input().split()))

nq, nk, np = queenarr[0], knightarr[0], pawnarr[0]
# 체스판에 놓기
for i in range(nq):
    x, y = queenarr[1 + i*2] - 1, queenarr[2 + i*2] - 1
    board[x][y] = 1
for i in range(nk):
    x, y = knightarr[1 + i*2] - 1, knightarr[2 + i*2] - 1
    board[x][y] = 1
for i in range(np):
    x, y = pawnarr[1 + i*2] - 1, pawnarr[2 + i*2] - 1
    board[x][y] = 1
unsafe += (nq + nk + np) # 말 놓인 칸들은 안전하지 않음

# 이제 각 Queen에 대해 8방향으로 위험구역 찾기
for i in range(nq):
    x, y = queenarr[1 + i*2] - 1, queenarr[2 + i*2] - 1
    # +x방향
    d = 1
    while x + d < n:
        # 안전구역이면 위험구역으로 변경
        if board[x+d][y] == 0:
            board[x+d][y] = 2
            unsafe += 1
        elif board[x+d][y] == 1:
            # 장애물부턴 더 나아가지 않음
            break
        d += 1
    # -x방향
    d = 1
    while x - d >= 0:
        # 안전구역이면 위험구역으로 변경
        if board[x-d][y] == 0:
            board[x-d][y] = 2
            unsafe += 1
        elif board[x-d][y] == 1:
            # 장애물부턴 더 나아가지 않음
            break
        d += 1
    # +y방향
    d = 1
    while y + d < m:
        # 안전구역이면 위험구역으로 변경
        if board[x][y+d] == 0:
            board[x][y+d] = 2
            unsafe += 1
        elif board[x][y+d] == 1:
            # 장애물부턴 더 나아가지 않음
            break
        d += 1
    # -y방향
    d = 1
    while y - d >= 0:
        # 안전구역이면 위험구역으로 변경
        if board[x][y - d] == 0:
            board[x][y - d] = 2
            unsafe += 1
        elif board[x][y - d] == 1:
            # 장애물부턴 더 나아가지 않음
            break
        d += 1
    # +x, +y방향
    d = 1
    while x + d < n and y + d < m:
        # 안전구역이면 위험구역으로 변경
        if board[x+d][y+d] == 0:
            board[x+d][y+d] = 2
            unsafe += 1
        elif board[x+d][y+d] == 1:
            # 장애물부턴 더 나아가지 않음
            break
        d += 1
    # +x, -y방향
    d = 1
    while x + d < n and y - d >= 0:
        # 안전구역이면 위험구역으로 변경
        if board[x+d][y-d] == 0:
            board[x+d][y-d] = 2
            unsafe += 1
        elif board[x+d][y-d] == 1:
            # 장애물부턴 더 나아가지 않음
            break
        d += 1
    # -x, +y방향
    d = 1
    while x - d >= 0 and y + d < m:
        # 안전구역이면 위험구역으로 변경
        if board[x-d][y+d] == 0:
            board[x-d][y+d] = 2
            unsafe += 1
        elif board[x-d][y+d] == 1:
            # 장애물부턴 더 나아가지 않음
            break
        d += 1
    # -x, -y방향
    d = 1
    while x - d >= 0 and y - d >= 0:
        # 안전구역이면 위험구역으로 변경
        if board[x-d][y-d] == 0:
            board[x-d][y-d] = 2
            unsafe += 1
        elif board[x-d][y-d] == 1:
            # 장애물부턴 더 나아가지 않음
            break
        d += 1
    

# 이제 각 knight에 대해 8가지 경우 보기
dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]
for i in range(nk):
    x, y = knightarr[1 + i*2] - 1, knightarr[2 + i*2] - 1
    for j in range(8):
        nx, ny = x + dx[j], y + dy[j]
        if (0 <= nx < n) and (0 <= ny < m) and board[nx][ny] == 0:
            board[nx][ny] = 2
            unsafe += 1

print(n * m - unsafe)