from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
d = deque()
for _ in range(n):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        d.appendleft(cmd[1])
    elif cmd[0] == 2:
        d.append(cmd[1])
    elif cmd[0] == 3:
        if not d: print(-1)
        else: print(d.popleft())
    elif cmd[0] == 4:
        if not d: print(-1)
        else: print(d.pop())
    elif cmd[0] == 5:
        print(len(d))
    elif cmd[0] == 6:
        if len(d) == 0: print(1)
        else: print(0)
    elif cmd[0] == 7:
        if len(d) == 0: print(-1)
        else: print(d[0])
    else: #8
        if len(d) == 0: print(-1)
        else: print(d[-1])
