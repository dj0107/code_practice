import sys
input = sys.stdin.readline
dig = 0b00000000000000000000
m = int(input())
cnt = 0
while cnt < m:
    cnt += 1
    order = input().split()
    target =  (2 ** (int(order[1])))
    if order[0] == 'add':
        if dig % target == 0:
            dig += target // 2
    elif order[0] == 'remove':
        if dig % target == 1:
            dig += target // 2
        lst[int(order[1])] = 0  
    elif order[0] == 'check':
        print(lst[int(order[1])])
    elif order[0] == 'toggle':
        lst[int(order[1])] += 1
        lst[int(order[1])] %= 2
    elif order[0] == 'all':
        lst = [1] * 21
    elif order[0] == 'empty':
        lst = [0] * 21