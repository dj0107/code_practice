
def find_root(x):
    if doked[x] != x:
        doked[x] = find_root(doked[x])
    
    return doked[x]

g = int(input())
p = int(input())
planes = [0] * (p+1)
doked = [k for k in range(g+1)]
for i in range(1, p+1):
    planes[i] = int(input())

cnt = 1

while cnt <= p:
    target = find_root(planes[cnt])
    if target == 0:
        break
    doked[target] = find_root(target - 1)
    cnt += 1

print(cnt - 1)