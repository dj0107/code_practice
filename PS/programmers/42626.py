import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) > 1:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        if first >= K: return answer
        new = first + 2*second
        heapq.heappush(scoville, new)
        answer += 1
    return -1 if scoville[0] < K else answer