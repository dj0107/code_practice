import sys
sys.setrecursionlimit(100001)

inorder = []
postorder = []
indic = {}
n = 0
answer = []
def solve(start, end, offset):
    global postorder, indic, answer # n 필요없을듯
    mid = indic[postorder[end]] - offset
    if start > end: return
    answer.append(postorder[end]) # mid에 해당하는거 넣기
    if end > start:
        solve(start, mid-1, offset)
        solve(mid, end-1, offset + 1)

n = int(input())
inorder = input().split()
postorder = input().split()


for i in range(n):
    indic[inorder[i]] = i

# 재귀적으로 대충 처리하면 됨
solve(0, n - 1, 0)
for i in range(n - 1):
    print(answer[i], end=' ')
print(answer[n-1])