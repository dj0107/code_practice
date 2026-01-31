class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.__value = value
        self.__next = next
        self.__prev = prev
    
    def getvalue(self):
        return self.__value
    def setvalue(self, value):
        self.__value = value
    def getnext(self):
        return self.__next
    def setnext(self, node):
        self.__next = node
    def getprev(self):
        return self.__prev
    def setprev(self, node):
        self.__prev = node
class DLL:
    def __init__(self):
        self.__header = Node(None, None, None)
        self.__trailer = Node(None, None, self.__header)
        self.__header.setnext(self.__trailer)
        self.__size = 0
    
    def __len__(self):
        return self.__size
    def __str__(self):
        elems = []
        cur = self.__header.getnext()        # 첫 실제 노드부터
        while cur is not self.__trailer:     # trailer 전까지
            elems.append(repr(cur.getvalue()))
            cur = cur.getnext()
        return '[' + ', '.join(elems) + ']'
    def isEmpty(self):
        return True if self.__size == 0 else False
        # return self.__size == 0
    def first(self): # None if empty
        return self.__header.getnext().getvalue()
    def last(self):  # None if empty
        return self.__trailer.getprev().getvalue()
    def addFirst(self, value):
        
        newest = Node(value, self.__header.getnext(), self.__header)
        self.__header.getnext().setprev(newest)
        self.__header.setnext(newest)
        self.__size += 1
    def addLast(self, value):
        newest = Node(value, self.__trailer, self.__trailer.getprev())
        self.__trailer.getprev().setnext(newest)
        self.__trailer.setprev(newest)
        self.__size += 1
    
    def removeFirst(self):
        if self.isEmpty():
            raise IndexError('you cannot remove from empty LL')
        answer = self.__header.getnext().getvalue()
        self.delete_node(self.__header.getnext())
        return answer
    def removeLast(self):
        if self.isEmpty():
            raise IndexError('you cannot remove from empty LL')
        answer = self.__trailer.getprev().getvalue()
        self.delete_node(self.__trailer.getprev())
        return answer
    
    def delete_node(self, node):
        predecessor = node.getprev()
        successor = node.getnext()
        predecessor.setnext(successor)
        successor.setprev(predecessor)
        self.__size -= 1
    def delete_at(self, idx):
        if idx >= self.__size:
            raise IndexError("there is no such index.")
        # if문으로 중간 이상이면 뒤에서, 이하면 앞에서 찾게 하면 조금 줄일 수 있긴 함
        tmp = self.__header.getnext()
        for i in range(idx):
            tmp = tmp.getnext()
        self.delete_node(tmp)
    
if __name__ == '__main__':
    myDLL = DLL()
    myDLL.addFirst(3)
    myDLL.addFirst(4)
    myDLL.addFirst(5)
    myDLL.addLast(1)
    myDLL.removeFirst()
    myDLL.delete_at(0)
    print(myDLL)