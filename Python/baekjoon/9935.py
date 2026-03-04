from collections import deque
s = input()
bomb = input()
destnum = len(bomb)
trigger = bomb[len(bomb) - 1]
q = deque() # 스택으로 사용
slen = len(s)
top = -1
for i in range(slen):
    
    q.append(s[i])
    top += 1
    if s[i] == trigger:
        bombed = True
        for j in range(1, destnum):
            if top - j < 0 or q[top - j] != bomb[len(bomb) - 1 - j]:
                bombed = False
                break
        
        if bombed:
            for j in range(destnum):
                q.pop()
                top -= 1

if top == -1:
    print("FRULA")
else:
    for e in q:
        print(e, end="")