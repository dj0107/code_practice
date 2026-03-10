import sys, heapq
input = sys.stdin.readline

n = int(input())
high, low = [], []
mid = [int(input()), None] # 원소 개수가 홀수면 None, 아니면 중간값 2개중 큰거
print(mid[0])
for i in range(1, n):
    num = int(input())
    if mid[1] is None: # 이전까지 홀수였던 경우(지금은 짝수)
        if num <= mid[0]:
            heapq.heappush(low, -num) # 음수로 넣어야 함
            mid[1] = mid[0] # mid 중 위로 올리기
            mid[0] = -heapq.heappop(low) # 덜 낮은 값을 빼야 함
        elif num > mid[0]:
            heapq.heappush(high, num)
            mid[1] = heapq.heappop(high)

    else: # 이전까지 짝수였던 경우(지금은 홀수)
        if num < mid[0]:
            heapq.heappush(low, -num)
            heapq.heappush(high, mid[1])
            mid[1] = None
        elif mid[0] <= num <= mid[1]:
            heapq.heappush(low, -mid[0])
            mid[0] = num
            heapq.heappush(high, mid[1])
            mid[1] = None
        else:
            heapq.heappush(high, num)
            heapq.heappush(low, -mid[0])
            mid[0] = mid[1]
            mid[1] = None

    print(mid[0])
