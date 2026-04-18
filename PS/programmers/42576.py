def solution(participant, completion):
    answer = ''
    n = len(participant)
    arr = {}
    #insert
    for player in participant:
        if player in arr.keys():
            arr[player] += 1
        else:
            arr[player] = 1
    # print(arr)
    # search
    for player in completion:
        if arr[player] > 1:
            arr[player] -= 1
        else:
            del arr[player]
            
    for keys in arr.keys():
        return keys


part = ["leo", "kiki", "eden"]
comp = ["eden", "kiki"]
solution(part, comp)