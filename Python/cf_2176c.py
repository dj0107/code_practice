t = int(input())
for i in range(t):
    n = int(input())
    # n = 200000
    arr = list(map(int, input().split()))
    # arr = [999999999] * 100000 + [1000000000] * 100000
    arr.sort()
    arr.reverse()
    odd = []
    even = []
    evenpointer = 0
    oddpointer = 0
    for j in arr:
        if j % 2 == 0:
            even.append(j)
        else:
            odd.append(j)

    evenNum = len(even)
    greedy = [0] * (n + 1)
    for k in range(1, n+1):
        if len(odd) == 0:
            continue
        elif k == 1:
            greedy[k] = odd[0]

        elif len(even) == 0:
            greedy[k] = odd[0] if k % 2 == 1 else 0
        elif k == 2:
            greedy[2] = (greedy[1] + even[0])
            
        
        else:
            if (k - evenNum) % 2 != 0 or k <= evenNum: # good
                
                evenpointer += 1
                if evenpointer == evenNum:
                    evenpointer -= 1
                greedy[k] = greedy[k - 1] + even[evenpointer]
                
                
            else:
                evenpointer -= 1
                oddpointer += 2
                if oddpointer != len(odd):
                    greedy[k] = greedy[k - 2]
    
    for j in range(1, n):
        print(greedy[j], end = " ")
    print(greedy[n])
        