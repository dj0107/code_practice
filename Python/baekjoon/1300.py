def counts(x, n): # x보다 작은 것들이 총 몇 개 있는지 알려줌
    ans = 0
    for i in range(1, n+1):
        if i > x: break
        ans += min(n, x // i)

    return ans



n = int(input())
k = int(input())

start, end = 1, k
result = 0
while start <= end:
    mid = (start + end) // 2
    num = counts(mid, n)
    if num < k:
        start = mid + 1
    elif num >= k:
        end = mid - 1
        result = mid

print(result)


