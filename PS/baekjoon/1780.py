import sys
input = sys.stdin.readline

def searchPaper(x, y, size):
    if size == 1: 
        count[paper[x][y]] += 1
        return


    prev = -2
    matched = True
    for i in range(size):
        for j in range(size):
            if prev != -2 and paper[x+i][y+j] != prev:
                matched = False
                break
            prev = paper[x+i][y+j]
    if matched:
        count[prev] += 1
        return
    else: 
        newSize = size // 3
        for i in range(3):
            for j in range(3):
                newx = x + (i * newSize)
                newy = y + (j * newSize)
                searchPaper(newx, newy, newSize)


n = int(input())
paper = []
count = {-1: 0, 0: 0, 1: 0}
for i in range(n):
    line = list(map(int, input().split()))
    paper.append(line)

searchPaper(0, 0, n)
print(count[-1])
print(count[0])
print(count[1])