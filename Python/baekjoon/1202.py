import heapq, sys
input = sys.stdin.readline

n, k = map(int, input().split())
bags, gems = [], []
for _ in range(n):
    m, v = map(int, input().split())
    gems.append((m, v))

for _ in range(k):
    w = int(input())
    bags.append(w)

bags.sort()
gems.sort()
ans = 0
lastGem = 0
pq = []
for bag in bags:

    while lastGem < n and gems[lastGem][0] <= bag:
        heapq.heappush(pq, -gems[lastGem][1]) # 조건은 만족을 해서 더 이상 무게는 상관x
        lastGem += 1
    
    if pq:
        ans -= heapq.heappop(pq)

print(ans)