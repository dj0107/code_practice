from collections import deque
def solution(rc, operations):
    n = len(rc)
    m = len(rc[0])
    lp = deque([rc[i][0] for i in range(n)])
    rp = deque([rc[i][-1] for i in range(n)])
    rows = deque(deque(rc[i][1:m-1]) for i in range(n))
    for operation in operations:
        if operation == 'ShiftRow':
            shiftrow(rows, lp, rp)
        else:
            rotate(rows, lp, rp)
    answer = []
    if len(rows[0]) != 0:
        for i in range(n):
            row = [lp[i]] + list(rows[i]) + [rp[i]]
            answer.append(row)
    else:
        for i in range(n):
            row = [lp[i]] + [rp[i]]
            answer.append(row)
    return answer
def shiftrow(rows, lp, rp):
    if len(rows[0]) != 0:
        rows.appendleft(rows.pop())
    lp.appendleft(lp.pop())
    rp.appendleft(rp.pop())
    
def rotate(rows, lp, rp):
    # right side
    tmp = rp.pop()
    if len(rows[0]) != 0:
        rp.appendleft(rows[0][-1])
    else:
        rp.appendleft(lp[0])
    # left side
    tmp2 = lp.popleft()
    if len(rows[0]) != 0:
        lp.append(rows[-1][0])
    else:
        lp.append(tmp)
    if len(rows[0]) != 0:
        # up side
        rows[0].pop()
        rows[0].appendleft(tmp2)
        # down side
        rows[-1].popleft()
        rows[-1].append(tmp)


arrr = [[1, 2], [3, 4]]
# ops = ["Rotate","ShiftRow"]
ops = ["Rotate"]
print(solution(arrr, ops))
        