def solution(players, m, k):
    answer = 0
    off = [0] * k
    now = 0
    for i in range(24):
        now -= off[i % k]
        off[i % k] = 0
        if players[i] >= (now + 1) * m:
            req = (players[i] // m) - now
            now += req
            off[i % k] = req
            answer += req
    return answer

play = [0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5]
m = 3
k = 5
print(solution(play, m, k))