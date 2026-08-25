def solution(friends, gifts):

    giftmap = {}
    final, giftpoints = {}, {}
    for friend in friends:
        giftmap[friend] = {}
        final[friend] = 0
        giftpoints[friend] = 0
    for gift in gifts:
        gift_from, gift_to = gift.split(" ")
        if gift_to not in giftmap[gift_from]: giftmap[gift_from][gift_to] = 0
        giftmap[gift_from][gift_to] += 1
        giftpoints[gift_from] += 1
        giftpoints[gift_to] -= 1

    num_friend = len(friends)
    
    for i in range(num_friend):
        for j in range(i+1, num_friend):
            # friends[i]와 friends[j]를 비교해서 final에 +1
            # 두 사람이 선물을 주고받았다면
            if ((friends[j] in giftmap[friends[i]]) or (friends[i] in giftmap[friends[j]])):
                # 우선 한 쪽만 줬을 수도 있으니 그 케이스 처리
                if (friends[j] not in giftmap[friends[i]]): # i가 j한테 준 적이 없으면 j만 줬으니 j가 1점 득점
                    final[friends[j]] += 1
                elif (friends[i] not in giftmap[friends[j]]): # j가 i한테 준 적이 없으면 i만 줬으니 i가 1점 득점
                    final[friends[i]] += 1
                elif (giftmap[friends[i]][friends[j]] < giftmap[friends[j]][friends[i]]):
                    final[friends[j]] += 1
                elif (giftmap[friends[j]][friends[i]] < giftmap[friends[i]][friends[j]]):
                    final[friends[i]] += 1

            # 두 사람이 서로 선물을 주고받은 적이 없거나 그 횟수가 같다면
            if ((friends[j] not in giftmap[friends[i]]) and (friends[i] not in giftmap[friends[j]])) or \
                (((friends[j] in giftmap[friends[i]]) and (friends[i] in giftmap[friends[j]])) and (giftmap[friends[i]][friends[j]] == giftmap[friends[j]][friends[i]])):
                if giftpoints[friends[i]] > giftpoints[friends[j]]: final[friends[i]] += 1
                if giftpoints[friends[i]] < giftpoints[friends[j]]: final[friends[j]] += 1

    answer = 0
    for score in final.values():
        answer = max(answer, score)
    
    
    return answer

friends = ["joy", "brad", "alessandro", "conan", "david"]
gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
print(solution(friends, gifts))