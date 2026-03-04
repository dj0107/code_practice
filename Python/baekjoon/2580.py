from collections import deque

sudoku = []
for _ in range(9):
    sudoku.append(list(map(int, input().split())))

q = deque()
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            q.append((i, j))
cnt = 0
threshold = 1
while q:
    cnt += 1
    if cnt == 300: threshold = 9
    x, y = q.popleft()
    row, col, sq = [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # targetsq = (x // 3, y // 3)
    for i in range(9):
        if sudoku[x][i] != 0: row.remove(sudoku[x][i])
        if sudoku[i][y] != 0: col.remove(sudoku[i][y])
    sqx, sqy = x - x % 3, y - y % 3
    for i in range(3):
        for j in range(3):
            if sudoku[sqx+i][sqy+j] != 0: sq.remove(sudoku[sqx+i][sqy+j])
    if 0 < len(row) <= threshold : sudoku[x][y] = row[0]
    elif 0 < len(col) <= threshold : sudoku[x][y] = col[0]
    elif 0 < len(sq) <= threshold : sudoku[x][y] = sq[0]
    else: q.append((x, y))
# print("==================")
for i in range(9):
    for j in range(9):
        print(sudoku[i][j], end=" ")
    print()

