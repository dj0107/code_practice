import sys
sys.setrecursionlimit = 10000000
input = sys.stdin.readline
def findRoot(node):
    if node != parent[node]:
        parent[node] = findRoot(parent[node])
    return parent[node]

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for i in range(m):
    op, a, b = map(int, input().split())
    root_a = findRoot(a)
    root_b = findRoot(b)
    # root_a , root_b = arr[a], arr[b]
    # while root_a != a:
    #     a = root_a
    #     root_a = arr[root_a]

    # while root_b != b:
    #     b = root_b
    #     root_b = arr[root_b]

    if op == 1:
        
        if root_a == root_b:
            print("YES")
        else:
            print("NO")
    elif op == 0:
        if root_a < root_b:
            parent[root_b] = root_a
        elif root_a > root_b:
            parent[root_a] = root_b
