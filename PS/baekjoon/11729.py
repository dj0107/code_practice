def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return
    mid = 6 - start - end
    hanoi(n-1, start, mid)
    print(start, end)
    hanoi(n-1, mid, end)


k = int(input())
print(2 ** k - 1)
hanoi(k, 1, 3)