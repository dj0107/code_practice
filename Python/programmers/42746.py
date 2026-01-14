def solution(numbers):
    arr = list(map(str, numbers))
    myMergeSort(arr)
    sted = list(reversed(arr))

    answer = ''
    for i in range(len(sted)):
        answer += sted[i]
    if int(answer) == 0:
        answer = '0'
    return answer

def myMergeSort(arr):
    n = len(arr)
    if n < 2:
        return
    mid = n // 2
    arr1 = arr[0:mid]
    arr2 = arr[mid:n]
    # print(arr1)
    # print(arr2)

    myMergeSort(arr1)
    myMergeSort(arr2)

    myMerge(arr1, arr2, arr)
    

def myMerge(arr1, arr2, arr):
    i = j = 0
    while i + j < len(arr):
        if j == len(arr2) or (i < len(arr1) and arr1[i] + arr2[j] < arr2[j] + arr1[i]):
            arr[i+j] = arr1[i]
            i += 1
        # elif i == len(arr1):
        #     arr[i+j] = arr2[j]
        #     j += 1
        else:
            
            arr[i+j] = arr2[j]
            j += 1
print(solution([0, 0, 0, 0]))
# print("123" > "2")
# b =  '3'
# c = '<5'
# a = format("asdf", b+c)
# print(a)
# print(myMergeSort(['1', '2', '3', '4']))