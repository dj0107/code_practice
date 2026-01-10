class Stack:
    def __init__(self):
        self.__st = []
        self.__cnt = 0
    def push(self, X):
        self.__st.append(X)
        self.__cnt += 1
    def pop(self):
        if self.__cnt == 0:
            return -1
        else:
            tmp = self.__st[self.__cnt - 1]
            del self.__st[self.__cnt - 1]
            self.__cnt -= 1
            return tmp
    def size(self):
        return self.__cnt
    def empty(self):
        return 1 if self.__cnt == 0 else 0
    def top(self):
        return -1 if self.__cnt == 0 else self.__st[self.__cnt - 1]
    

N = int(input())
st = Stack()
for i in range(N):
    order = input().split()
    if order[0] == "push":
        st.push(order[1])
    elif order[0] == "pop":
        print(st.pop())
    elif order[0] == "size":
        print(st.size())
    elif order[0] == "empty":
        print(st.empty())
    elif order[0] == "top":
        print(st.top())