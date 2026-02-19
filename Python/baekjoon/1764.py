import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
hear = {}
watch = {}
for _ in range(n):
    ppl = input().rstrip()
    hear[ppl] = 1
for _ in range(m):
    ppl = input().rstrip()
    watch[ppl] = 1
hearwatch = []
for hears in hear:
    if hears in watch: hearwatch.append(hears)

hearwatch.sort()
# print(hearwatch)
# for people in hearwatch:
#     print(people)
print(len(hearwatch))
for i in range(len(hearwatch)):
    print(hearwatch[i])