def solution(nums):
    answer = 0
    poke = [0] * 200001
    for i in nums:
        poke[i] += 1
    for i in range(200001):
        if poke[i] != 0:
            answer += 1
    answer = min(len(nums)/2, answer)
    return answer