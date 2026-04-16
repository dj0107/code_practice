n, l = map(int, input().split())
position = list(map(int, input().split()))
position.sort()
position.insert(0, 0)
position.append(l)
maxdistance = 0
for i in range(len(position) - 1):
    maxdistance = max(maxdistance, \
                      position[i + 1]\
                          - position[i])

print(max(maxdistance / 2, position[1], l - position[-2]))