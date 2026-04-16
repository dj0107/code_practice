n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

def dfs(start, remain, visit):
    global nums
    if remain == 0:
        print(*visit)
        return
    for next in nums:
        if next not in visit:
            nextvisit = visit[:] + [next]
            dfs(next, remain - 1, nextvisit)
    


for i in range(1, n+1):
    dfs(i, m - 1, [i])
