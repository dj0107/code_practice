from collections import deque

def process():
    # step 1: rotate with robots
    dura.appendleft(dura.pop())
    # 로봇 위치 조정
    tmp = deque()
    for rob in robot:
        if rob != n-2: tmp.append((rob + 1) % (2*n - 1))
    robot = tmp
    


n, threashold = map(int, input().split())
dura = list(map(int, input().split()))
dura = deque(dura)
robot = deque()
