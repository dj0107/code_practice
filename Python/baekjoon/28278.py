import sys
input = sys.stdin.readline

def push(stk, x):
    stk.append(x)

def pop(stk):
    if len(stk) == 0: 
        print(-1)
        return
    ret = stk[len(stk) - 1]
    del stk[len(stk) - 1]
    print(ret)

def leng(stk):
    print(len(stk))

def empty(stk):
    if len(stk) == 0: 
        print(1)
        return
    print(0)
def top(stk):
    if len(stk) == 0: 
        print(-1)
        return
    print(stk[len(stk) - 1])

stk = []

n = int(input())
for _ in range(n):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        push(stk, cmd[1])
    elif cmd[0] == 2:
        pop(stk)
    elif cmd[0] == 3:
        leng(stk)
    elif cmd[0] == 4:
        empty(stk)
    else:
        top(stk)

