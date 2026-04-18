import math

def solution(n, k):
    answer = 0
    kth = ''
    while n > 0:
        re = n % k
        n = n // k
        kth = str(re) + kth
    
    arr = kth.split('0')
    # print(arr)
    for e in arr:
        if e != '':
            target = int(e)
        else:
            target = 0
        answer += isPrime(target)
    return answer
def isPrime(n):

    if n <= 1:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    
    return 1
print(solution(437674, 3))
for i in range(1, 10, 2):
    print(i)