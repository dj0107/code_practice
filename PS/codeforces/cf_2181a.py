import math
import sys

input = sys.stdin.readline

answer = []

n, m = map(int, input().split())  # 200000, 500000

city = []
city_cnt = []              # 각 도시별 알파벳 빈도 [26]
whole_cnt = [0] * 26       # 전체 알파벳 빈도

for _ in range(n):
    s = input().strip()
    city.append(s)

    cnt = [0] * 26
    for ch in s:          # 한 번만 순회해서 도시/전체 빈도 모두 갱신
        idx = ord(ch) - 65
        cnt[idx] += 1
        whole_cnt[idx] += 1

    city_cnt.append(cnt)

for i in range(n):
    req = 0
    unable = False

    # A~Z 26개만 순회
    for idx in range(26):
        mine = city_cnt[i][idx]
        rest = whole_cnt[idx] - mine

        if rest == 0 and mine > 0:
            unable = True
            # 더 볼 필요 없음
            break
        elif rest != 0 and mine > 0:
            # math.ceil(mine / ingredient)
            req = max(req, (mine + rest - 1) // rest)


    if unable or req > m:
        answer.append(-1)
    else:
        answer.append(m - req)

# 출력
print(" ".join(map(str, answer)))