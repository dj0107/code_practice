def solution(n):
    answer = [[-1]*n for i in range(n)]
    diry = [1, 0, -1, 0]
    dirx = [0, 1, 0, -1]
    dir = 0
    currentx = 0
    currenty = 0
    for i in range(1, n**2 + 1):
        answer[currentx][currenty] = i

        x = currentx + dirx[dir]
        y = currenty + diry[dir]

        if x > n - 1 or x < 0 or y > n - 1 or \
        y < 0 or answer[x][y] != -1:
            dir = (dir + 1) % 4
        
        currentx = currentx + dirx[dir]
        currenty = currenty + diry[dir]

        

    return answer

print(solution(4))