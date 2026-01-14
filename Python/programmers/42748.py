def solution(array, commands):
    answer = []

    for a in range(len(commands)):
        i = commands[a][0]
        j = commands[a][1]
        k = commands[a][2]
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

print(solution([1, 2, 3], [[1, 3, 3]]))