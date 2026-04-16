INF = float('inf')

n, m = map(int, input().split())
prices = {"LOVE": INF}
for _ in range(n):
    element, price = input().split()
    prices[element] = int(price)
formulas = [] # [생성물, (요구랑1, 재료1), ...,(요구량n, 재료n)] 을 저장
for _ in range(m): # 최초 공식 스캔으로 파싱하고 사전에 등록(일단은 무한대로)
    formula = input().replace('=', '+').split('+')
    result = formula[0]
    if result not in prices: prices[result] = INF
    row = [result]
    for i in range(1, len(formula)):
        reqNum, name = int(formula[i][0]), formula[i][1:] 
        row.append((reqNum, name))
        if name not in prices:
            prices[name] = INF
    
    formulas.append(row)
# row: [생성물, (요구랑1, 재료1), ...,(요구량n, 재료n)] 을 저장
for _ in range(50):
    for row in formulas:
        sum = 0
        for i in range(1, len(row)):
            sum += row[i][0] * prices[row[i][1]]
        prices[row[0]] = min(prices[row[0]], sum)

if prices["LOVE"] == INF: print(-1)
elif prices["LOVE"] > 1000000000: print(1000000001)
else: print(prices["LOVE"])