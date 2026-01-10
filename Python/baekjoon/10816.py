n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))
cards.sort()
snums = sorted(nums)
ans = []

# for i in range(0, len(nums)):
#     point = 0
#     start = 0
#     end = n - 1
#     mid = (start + end) // 2
#     cnt = 0
#     while (start <= end):
#         if cards[mid] == nums[i]:
#             cnt = 1
#             break
#         elif cards[mid] < nums[i]:
#             start = mid + 1
#             mid = (start + end) // 2
#         else:
#             end = mid - 1
#             mid = (start + end) // 2
#     midd = mid
#     if cnt == 1:
#         while midd >= 1 and cards[midd - 1] == nums[i]:
#             cnt += 1
#             midd -= 1
#         midd = mid
#         while midd < n - 1 and cards[midd + 1] == nums[i]:
#             cnt += 1
#             midd += 1
#     print(cnt, end = " ")

ncnt = 0
ccnt = 0
while ncnt < len(snums):
    matched = 0
    same = 0
    while ncnt < len(snums) - 1 and snums[ncnt] == snums[ncnt + 1]:
        same += 1
        ncnt += 1
    while ccnt < len(cards) and cards[ccnt] <= snums[ncnt]:
        if cards[ccnt] == snums[ncnt]:
            matched += 1
            # print("matched", ccnt, ncnt)
        ccnt += 1
    
    # apply
    for k in range(0, same + 1):
        ans.append(matched)
    # print(ans)    
    ncnt += 1

# 찾아서 ans의 적절한 곳 출력

for i in range(0, len(nums)):
    point = 0
    start = 0
    end = m - 1
    mid = (start + end) // 2
    while (start <= end):
        if snums[mid] == nums[i]:
            break
        elif snums[mid] < nums[i]:
            start = mid + 1
            mid = (start + end) // 2
        else:
            end = mid - 1
            mid = (start + end) // 2
    
    print(ans[mid], end=" ")
#     print(ans[mid], mid)
    
# print(snums)



