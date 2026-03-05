n, m = map(int, input().split())
cnt = 0
while m != n:
    cnt += 1
    if m % 2 == 1 or m < n:
        m += 1
    else:
        m = m // 2
print(cnt)