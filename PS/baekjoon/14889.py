def DFS(player):
    if len(player) == n: 
        solve(player)
        
    for i in range(player[-1] + 1, n):
        return DFS(player + [i])

def solve(player):
    sum = 0
    for i in range(1, n+1):
        if i in player: 

n = int(input())
minval = float('inf')
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

