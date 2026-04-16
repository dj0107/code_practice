def solution(clothes):
    answer = 1
    arr = {}
    n = len(clothes)
    for i in range(n):
        ctype = clothes[i][1]
        cname = clothes[i][0]
        arr[ctype] = arr.get(ctype, 0) + 1
    
    for num in arr.values():
        answer *= (num + 1)
    answer -= 1
    return answer