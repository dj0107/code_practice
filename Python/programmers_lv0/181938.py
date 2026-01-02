def solution(a, b):
    answer = 0

    superplus = a * (10 ** len(str(b))) + b
    producttwo = 2 * a * b
    answer = max(superplus, producttwo)
    return answer