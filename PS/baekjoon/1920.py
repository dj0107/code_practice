n = int(input())
arr = list(map(int, input().split()))
m = int(input())
query = list(map(int, input().split()))

arr.sort()
for i in range(0, m):
    start = 0
    end = n - 1
    mid = (start + end) // 2
    ans = 0

    while (start <= end):
        if query[i] < arr[mid]:
            end = mid - 1
            mid = (start + end) // 2
        elif query[i] > arr[mid]:
            start = mid + 1
            mid = (start + end) // 2
        elif query[i] == arr[mid]:
            ans = 1
            break
    
    print(ans)