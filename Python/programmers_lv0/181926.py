def solution(n, control):
    answer = n
    for i in range(len(control)):
        move = control[i]
        if move == 'w':
            answer = answer + 1
        elif move == 's':
            answer = answer - 1
        elif move == 'd':
            answer = answer + 10
        else:
            answer = answer - 10
    return answer