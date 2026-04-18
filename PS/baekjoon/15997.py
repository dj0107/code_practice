country = input().split()

match1 = input().split()
match2 = input().split()
match3 = input().split()
match4 = input().split()
match5 = input().split()
match6 = input().split()
go = {}
for c in country: go[c] = 0
for m1 in range(2, 5):
    for m2 in range(2, 5):
        for m3 in range(2, 5):
            for m4 in range(2, 5):
                for m5 in range(2, 5):
                    for m6 in range(2, 5):
                        rate = float(match1[m1]) * \
                            float(match2[m2]) * float(match3[m3]) * \
                                float(match4[m4]) * float(match5[m5]) \
                                    * float(match6[m6])
                        if rate == 0: continue
                        points = {}
                        for c in country: points[c] = 0
                        # 승점 계산
                        if m1 == 2: points[match1[0]] += 3
                        elif m1 == 3: 
                            points[match1[0]] += 1
                            points[match1[1]] += 1
                        else: points[match1[1]] += 3

                        if m2 == 2: points[match2[0]] += 3
                        elif m2 == 3: 
                            points[match2[0]] += 1
                            points[match2[1]] += 1
                        else: points[match2[1]] += 3

                        if m3 == 2: points[match3[0]] += 3
                        elif m3 == 3: 
                            points[match3[0]] += 1
                            points[match3[1]] += 1
                        else: points[match3[1]] += 3

                        if m4 == 2: points[match4[0]] += 3
                        elif m4 == 3: 
                            points[match4[0]] += 1
                            points[match4[1]] += 1
                        else: points[match4[1]] += 3

                        if m5 == 2: points[match5[0]] += 3
                        elif m5 == 3: 
                            points[match5[0]] += 1
                            points[match5[1]] += 1
                        else: points[match5[1]] += 3

                        if m6 == 2: points[match6[0]] += 3
                        elif m6 == 3: 
                            points[match6[0]] += 1
                            points[match6[1]] += 1
                        else: points[match6[1]] += 3
                        # print("points:" , points, "rate:", rate)
                        # 확률 더해주기
                        lst = []
                        for c, point in points.items():
                            lst.append((point, c))
                        lst.sort(reverse=True)
                        if lst[0][0] == lst[3][0]: # 모두 동점
                            for c in go: go[c] += rate / 2 # 절반 확률
                        elif lst[0][0] == lst[2][0]: # 공동1등 3명
                            for i in range(3):
                                go[lst[i][1]] += rate * 2 / 3
                        elif lst[1][0] == lst[3][0]: # 공동 2등 3명
                            go[lst[0][1]] += rate
                            for i in range(1, 4):
                                go[lst[i][1]] += rate / 3
                        elif lst[1][0] == lst[2][0]: # 공동 2등 2명
                            go[lst[0][1]] += rate
                            for i in range(1, 3):
                                go[lst[i][1]] += rate / 2
                        else:
                            for i in range(2):
                                go[lst[i][1]] += rate

for i in range(4):
    print(go[country[i]])