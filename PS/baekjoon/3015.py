import sys
input = sys.stdin.readline
n = int(input())
stk = []
num = 0
matched = 0
for i in range(n):
    height = int(input())
    # stk.append(psn)
    streak = 1
    while len(stk) != 0:
        if stk[-1][0] < height:
            matched += 1
            stk.pop()
        elif stk[-1][0] == height:
            if stk[0][0] == height:
                matched -= 1
            streak = stk[-1][1] + 1
            matched += streak
            break
        else:
            matched += 1
            break

    stk.append((height, streak))

print(matched)

    

    
        
