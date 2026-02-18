class Node:
    def __init__(self, value=None, next=None):
        self.__value = value
        self.__next = next
    def getvalue(self):
        return self.__value
    def setvalue(self, value):
        self.__value = value
    def getnext(self):
        return self.__next
    def setnext(self, node):
        self.__next = node
class SLL:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
    
    def __len__(self):
        return self.__size
    def isEmpty(self):
        return True if self.__size == 0 else False
        # return self.__size == 0
    def first(self):
        if self.isEmpty():
            raise IndexError('no element in LL')
        return self.__head.getvalue()
    def last(self):
        if self.isEmpty():
            raise IndexError('no element in LL')
        return self.__tail.getvalue()
    def addFirst(self, value):
        if self.isEmpty():
            newest = Node(value, None)
            self.__head = newest
            self.__tail = newest
        else:
            newest = Node(value, self.__head)
            self.__head = newest
        self.__size += 1
    def addLast(self, value):
        if self.isEmpty():
            newest = Node(value, None)
            self.__head = newest
            self.__tail = newest
        else:
            newest = Node(value, None)
            self.__tail.setnext(newest)
            self.__tail = newest
        self.__size += 1
    
    def removeFirst(self):
        if self.isEmpty():
            raise IndexError('you cannot remove from empty LL')
        answer = self.__head.getvalue()
        # 누구에게도 참조되지 않는 self.__head()는 파이썬의 경우 GC가 알아서 제거
        # C++ 등 몇몇 PL이었다면 del이 필요했을 것
        self.__head = self.__head.getnext()
        self.__size -= 1
        if self.isEmpty():
            self.__tail = None
        return answer

