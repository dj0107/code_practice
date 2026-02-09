
n = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))

greedy = [0, road[0] * city[0]]
bestPrice = min(city[0], city[1])

for i in range(2, n):
    # if bestPrice <= city[i-1]:
    #     greedy.append(greedy[-1] + road[i-1]*bestPrice)
    # else:
    bestPrice = min(bestPrice, city[i-1])
    greedy.append(greedy[-1] + road[i-1]*bestPrice)

print(greedy[-1])
