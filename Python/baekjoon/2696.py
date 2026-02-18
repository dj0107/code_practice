import heapq
t = int(input())
for _ in range(t):
    m = int(input())
    arr = []
    for i in range(m // 10 + 1):
        tmp = list(map(int, input().split()))
        arr += tmp
    
    ans = [arr[0]]
    mid = arr[0]
    low, high = [], []

    # 이제부터 2개씩 읽음
    i = 1
    while i < m:
        v1, v2 = arr[i], arr[i+1]

        if v1 >= mid and v2 >= mid:
            heapq.heappush(high, v1)
            heapq.heappush(high, v2)
            tmp, mid = mid, heapq.heappop(high)
            heapq.heappush(low, -tmp)
        elif v1 <= mid and v2 <= mid:
            heapq.heappush(low, -v1)
            heapq.heappush(low, -v2)
            tmp, mid = mid, -heapq.heappop(low)
            heapq.heappush(high, tmp)

        else:
            lowval = min(v1, v2)
            highval = max(v1, v2)
            heapq.heappush(low, -lowval)
            heapq.heappush(high, highval)

        ans.append(mid)
        i += 2
    print(len(ans))
    for i in range(1, len(ans)+1):
        print(ans[i-1], end=" ")
        if i % 10 == 0: print("")
    if len(ans) % 10 != 0:
        print("")