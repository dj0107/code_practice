def solution(n):
    now = n
    answer = []
    while True:
        answer.append(now)
        if now == 1:
            break
        elif now % 2 == 0:
            now = now / 2
        else:
            now = now * 3 + 1
    return answer