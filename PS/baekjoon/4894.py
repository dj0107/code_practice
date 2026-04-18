PI = 3.141
itered = 0
while True:
    n = input()
    if n == "": continue
    elif n == "0": break
    n = int(n)
    itered += 1
    # 직선 거리 말고 제곱 거리로 일단 표현해보기
    dist1 = []
    dist2 = []
    t1x, t1y, t2x, t2y, energy = map(float, input().split())
    energy = energy / PI
    
    for i in range(n):
        mx, my = map(float, input().split())
        dis1 = (mx - t1x) ** 2 + (my - t1y) ** 2
        dis2 = (mx - t2x) ** 2 + (my - t2y) ** 2
        dist1.append((dis1, i))
        dist2.append((dis2, i))
    dist1.sort()
    dist2.sort()

    # dist1.insert(0, 0.0)
    answer = 0
    includes = []
    for i in range(n):
        remain = energy - dist1[i][0]
        if remain < 0: break
        includes.append(dist1[i][1]) # index를 넣기
        included = i+1
        
        for j in range(n):

            if remain >= dist2[j][0] and dist2[j][1] not in includes: # 더 넣을 수 있다면
                included += 1
        answer = max(included, answer)
    
    # t1에 에너지 안주는 경우도 처리
    included = 0
    includes = []
    for i in range(n):
        if dist1[i][0] == 0: 
            included += 1
            includes.append(dist1[i][1])

    for i in range(n):
        if dist2[i][0] <= energy and dist2[i][1] not in includes:
            included += 1
            includes.append(dist2[i][1])

    answer = max(answer, included)

    # t2에 에너지 안주는 경우도 처리 (아마 필요없음)
    included = 0
    includes = []
    for i in range(n):
        if dist2[i][0] == 0: 
            included += 1
            includes.append(dist2[i][1])

    for i in range(n):
        if dist1[i][0] <= energy and dist1[i][1] not in includes:
            included += 1
            includes.append(dist1[i][1])

    answer = max(answer, included)

    print(itered,". " ,n - answer, sep="")