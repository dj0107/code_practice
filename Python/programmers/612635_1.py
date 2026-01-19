# skill test lv2

def solution(clothes):
    answer = 1
    cdict = {}
    for cloth in clothes:
        cdict[cloth[1]] = cdict.get(cloth[1], 0) + 1
    
    for x in cdict.values():
        answer *= x+1
    answer -= 1
    return answer