n = int(input())
inorder = input().split()
postorder = input().split()

indic = {}
for i in range(n):
    indic[inorder[i]] = i

# 재귀적으로 대충 처리하면 됨