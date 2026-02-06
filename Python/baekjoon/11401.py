# def comb(n, k):
#     global combdic
#     if (n, k) in combdic.keys():
#         return combdic[(n, k)]
#     if k == 1 or k == n - 1: return n
#     if k == 0 or k == n: return 1

#     sum = 0
#     tmp = n - 1
#     while tmp >= k-1:
#         sum += comb(tmp, k-1)
#         tmp -= 1
#     combdic[(n, k)] = sum
#     return sum
    
# n, k = map(int, input().split())
# combdic = {}
# combdic[(0, 0)], combdic[(1, 0)], combdic[(1, 1)] = 1, 1, 1


# print(comb(n, k))
## 느림.
