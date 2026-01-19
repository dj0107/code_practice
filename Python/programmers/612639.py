def solution(gems):
    answer = []

    n = len(gems)
    dic = {}
    num = 0
    for e in gems:
        if e not in dic.keys():
            dic[e] = 0
            num += 1
    right = 0
    left = 0
    gmin = n
    foundnum = 0
    while right < n:
        if foundnum == num:
            if left == n - 1:
                break
            else:
                dic[gems[left]] -= 1
                if dic[gems[left]] == 0:
                    foundnum -= 1
                else:
                    gmin = min(gmin, right - left + 1)
                left += 1

        else:
            if right == n-1:
                break
            else:
                right += 1
                dic[gems[right]] += 1
                if dic[gems[right]] == 1:
                    foundnum += 1
                if foundnum == num:
                    gmin = min(gmin, right - left + 1)
                

            





    return answer