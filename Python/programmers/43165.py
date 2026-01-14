def solution(numbers, target):
    answer = 0
    cnt = 0
    n = len(numbers)
    while cnt < 2 ** n:
        sum = 0
        now = format(bin(cnt)[2:], '0>' + str(n))
        for i in range(n):
            mul = 1 if now[i] == '0' else -1
            sum += mul * numbers[i]
        # print(sum)
        if sum == target:
            answer += 1

        cnt += 1
    return answer
print(solution([4, 1, 2, 1], 4))