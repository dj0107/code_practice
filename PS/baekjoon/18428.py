n = int(input())

maze = []
for _ in range(n):
    line = input().split()
    maze.append(line)

# 걍 DFS