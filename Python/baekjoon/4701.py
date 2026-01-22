def checkName(names, st):
    ans = 0
    for name in names:
        if st > name: ans += 1
    return ans

while True:
    n = int(input())
    if n == 0: break
    names = []
    for i in range(n):
        st = input()
        names.append(st)
    names.sort()
    # print(names)
    answer = ''
    target = names[n // 2 - 1]
    l = len(target)
    for i in range(1, l+1):
        letter = target[:i]
        if letter >= target:
            answer = letter
            break
        char = target[i-1]
        next_char_code = ord(char) + 1
        next_char = chr(next_char_code)
        another = target[:i-1] + next_char
        if another < names[n // 2]:
            answer = another
            break
    print(answer)


