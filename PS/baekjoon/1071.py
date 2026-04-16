n = int(input())
arr = sorted(list(map(int, input().split())))

# prev, swapPoint = -1, -1
for _ in range(2500):
    
    for i in range(n-1):
        if arr[i] + 1 == arr[i+1]:
            swapPoint = -1
            for j in range(i+2, n): # 뒤에서 바꿀거 찾기
                if arr[i+1] != arr[j] and arr[i] != arr[j]: 
                    swapPoint = j
                    break
            if swapPoint != -1:
                arr[i+1], arr[swapPoint] =  arr[swapPoint], arr[i+1]
            else:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            continue


print(*arr)