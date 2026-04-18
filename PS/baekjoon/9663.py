
def DFS(x, y, placed):
    if x == n: return 1
    sum = 0
    # placed.append((x, y))
    # 다음 열에 놓을 게 없다면 0
    # impossible = True
    for i in range(1, n+1): # (x+1, i)를 점검
        found = True
        for px, py in placed:
            if i == py or x+1-px == abs(i-py):
                found = False
                break
        if found:
            # impossible = False
            sum += DFS(x+1, i, placed + [(x+1, i)])

    # if impossible: return 0
    return sum

n = int(input())
sum = 0
for i in range(1, n+1):
    sum += DFS(1, i, [(1, i)])

print(sum)