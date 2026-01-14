def solution(num_list):


    answer = 0

    productSum = 1
    squareSum = 0

    for i in range(len(num_list)):
        productSum *= num_list[i]
        squareSum += num_list[i]
    squareSum *= squareSum

    answer = 1 if productSum < squareSum else 0
    return answer