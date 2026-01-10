from collections import deque

n, m = map(int, input().split())
chessboard = [[0]*m for i in range(n)]
for i in range(n):
    row = input()
    for j in range(m):
        chessboard[i][j] = row[j]

to_traverse = deque()
# 기본 서치
for i in range(n):
    for j in range(m):
        if chessboard[i][j] == '.':
            chessboard[i][j] = "B"
            # BFS 
            mode = 'W'
            if i > 0 and chessboard[i - 1][j] == '.':
                to_traverse.append([i - 1, j])
            if i < n - 1 and chessboard[i + 1][j] == '.':
                to_traverse.append([i + 1, j])
            if j > 0 and chessboard[i][j - 1] == '.':
                to_traverse.append([i, j - 1])
            if j < m - 1 and chessboard[i][j + 1] == '.':
                to_traverse.append([i, j + 1])
            to_traverse.append(['c', 'c']) # checkpoint

            while to_traverse: # loop until it is empty
                popped = to_traverse.popleft()
                if popped[0] == 'c' and to_traverse:
                    mode = 'W' if mode == 'B' else 'B' # mode switch
                    to_traverse.append(['c', 'c']) # new checkpoint
                elif popped[0] == 'c':
                    pass
                else:
                    x = popped[0]
                    y = popped[1]
                    chessboard[x][y] = mode
                    if x > 0 and chessboard[x - 1][y] == '.':
                        to_traverse.append([x - 1, y])
                    if x < n - 1 and chessboard[x + 1][y] == '.':
                        to_traverse.append([x + 1, y])
                    if y > 0 and chessboard[x][y - 1] == '.':
                        to_traverse.append([x, y - 1])
                    if y < n - 1 and chessboard[x][y + 1] == '.':
                        to_traverse.append([x, y + 1])
            
            
for i in range(n):
    for j in range(m):
        print(chessboard[i][j], end='')
    print("")