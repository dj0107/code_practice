from collections import deque

t = int(input())
state = 1

for i in range(t):
    q = deque(list(input()))
    state = 1
    while q:
        nxt = q.popleft()
        if state == 1:
            if nxt == '0': state = 6
            else: state = 2

        elif state == 2:
            if nxt == '0': state = 3
            else: 
                state = -1
                break
        elif state == 3:
            if nxt == '0': state = 4
            else: 
                state = -1
                break
        elif state == 4:
            if nxt == '0': state = 4
            else: state = 15
        elif state == 6:
            if nxt == '1': state = 17
            else: 
                state = -1
                break
        elif state == 15:
            if nxt == '0': state = 6
            else: state = 125
        elif state == 17:
            if nxt == '0': state = 6
            else: state = 2
        elif state == 36:
            if nxt == '0': state = 4
            else: state = 17
        elif state == 125:
            if nxt == '0': state = 36
            else: state = 125
    
    if state == 15 or state == 17 or state == 125:
        print("YES")
    else:
        print("NO")

# a = '1234'
# print(list(a))