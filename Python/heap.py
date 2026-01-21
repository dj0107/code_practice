import random
import time
# getter setter 번거로우므로 _으로 그냥 구현
def isRightmost(n: int) -> bool:
    # 1, 3, 7... 처럼 n+1이 2의 거듭제곱 형태라면 true
    if n < 1:
        return False
    n = n + 1
    while n > 1:
        if n % 2 != 0: return False
        n = n // 2
    return True


class Node:
    #__slots__ = '__value', '__'
    def __init__(self, key, value, left, right, parent):
        self._key = key
        self._value = value
        self._left = left
        self._right = right
        self._parent = parent

class HeapQ: # min_heap (부모의 키 값 <= 자식의 키 값)
    def __init__(self):
        self._root = None
        self._size = 0
        self._last = None
    def up_bubble(self, node:Node):
        """
        insert 되었을때 up-heap-bubbling을 위해 사용됨
        
        :param node: 막 insert 되어서 위로 swap해야 할 대상 노드
        """
        while node != self._root and node._parent._key > node._key: # swap
            print(f"up: swap {node._key}, {node._value} and {node._parent._key}, {node._parent._value}")
            node._key, node._parent._key = node._parent._key, node._key
            node._value, node._parent._value = node._parent._value, node._value
            node = node._parent

    def down_bubble(self):
        """
        root와 last가 swap 된 후에 root에 대해서 시작하는 함수
        """
        target = self._root
        run = True
        while run:
            if (target._left is None or target._left._key >= target._key)\
                and (target._right is None or target._right._key >= target._key): # 부모가 왼 자식보다도, 오른 자식보다도 작으면 끝
                run = False
            elif target._right is None or \
                (target._left and target._left._key < target._right._key):
                # 왼쪽으로 swap
                print(f"left: swap {target._key}, {target._value} and {target._left._key}, {target._left._value}")
                tmp = (target._key, target._value)
                target._key = target._left._key
                target._value  = target._left._value
                target = target._left
                target._key = tmp[0]
                target._value  = tmp[1]

            else: # 오른쪽으로 swap
                print(f"right: swap {target._key},{target._value}  and {target._right._key}, {target._right._value}")
                tmp = (target._key, target._value)
                target._key = target._right._key
                target._value  = target._right._value
                target = target._right
                target._key = tmp[0]
                target._value  = tmp[1]
        

    
    def add(self, key, value):

        # 빈 힙인 경우
        if self.isEmpty():
            self._root = Node(key, value, None, None, None)
            self._size += 1
            return

        if isRightmost(self._size):# 마지막 층이 꽉 찬 경우
            # 제일 왼쪽 노드에 자식 추가, last 지정
            target: Node = self._root


            while target._left != None:
                target = target._left
            newest = Node(key, value, None, None, target)
            target._left = newest
            self._last = newest
            
        else:
            # step 1: left child가 나올때까지 올라가고(자기 자신 포함)
            # !!!(앞서 root까지 올라가는 =막층이 꽉 찬 경우는 걸러냈음)
            # step 2: 그 left child의 부모의 right child, 즉 오른 형제를 찾고
            # step 3:left로 leaf까지 내려가기
            target = self._last
            # Step 1
            while target != target._parent._left:
                target = target._parent
            # Step 2
            #target = target._parent._right
            target = target._parent # 일단 부모로 가기
            # right가 None인 경우
            noright = False
            if target._right is None:
                noright = True
                newest = Node(key, value, None, None, target)
                target._right = newest
                self._last = newest
            else:
                target = target._right
            # Step 3
            while not noright and target._left is not None:
                target = target._left
            # 지금 target의 왼쪽 노드로 새 노드 만들어서 자식 삼기
            if not noright:
                newest = Node(key, value, None, None, target)
                target._left = newest
                self._last = newest

        self._size += 1

        # 이제 Up-Heap bubble 하기
        self.up_bubble(self._last)
        print(f"size: {self._size}, last: {self._last._key}, {self._last._value}")
    
    def isEmpty(self):
        return self._size == 0

    def remove_min(self) -> tuple[int, any]: 
        # 빈 경우
        if self.isEmpty():
            raise IndexError('there is no element to remove')
        if self._size == 1: # 루트만 있는 경우
            answer = (self._root._key, self._root._value)
            self._root = None
            self._last = None
            self._size = 0
            return answer

        # root와 last의 key, value 교환
        answer = (self._root._key, self._root._value)
        self._root._key = self._last._key
        self._root._value = self._last._value
        
        #self._last._key = answer[0]
        #self._last._value = answer[1] # 어차피 지울거라 없어도 됨
        # 지울거 미리 저장해놓기
        to_remove = self._last
        # last 노드 소멸 및 새로운 last 지정
        
        if isRightmost(self._size - 1): # 왼쪽 끝인 경우
            target = self._root
            while target._right != None:
                target = target._right
            self._last = target
        else:
            target = self._last
            # (본인 포함)right child 까지 올라가기
            while target != target._parent._right:
                target = target._parent
            # 왼쪽 형제로 이동
            target = target._parent._left
            # right child로 leaf 까지 이동
            while target._right is not None:
                target = target._right
            self._last = target

        self._size -= 1

        if to_remove._parent is not None:
            if to_remove._parent._left == to_remove:
                to_remove._parent._left = None
            else:
                to_remove._parent._right = None
        
        # 꼭대기부터 down-heap bubbling
        self.down_bubble()

        return answer
    def __len__(self):
        return self._size
    def min(self):
        return (self._root._key, self._root._value)


if __name__ == '__main__':
    # hq = HeapQ()
    # hq.add(31, 31)
    # hq.add(28, 28)
    # hq.add(44, 44)
    # hq.add(47, 47)
    # hq.add(15,15)
    # hq.add(34,34)
    # for i in range(len(hq)):
    #     print(hq.remove_min())
    # f = open('sorttest.txt','w')
    # for i in range(100000):
    #     line = str(random.randint(0, 999999)) + '\n'
    #     f.write(line)
    # f.close()
    arr1 = []
    arr2 = []
    f = open('sorttest.txt', 'r')
    for line in f:
        if line != '':
            arr1.append(line)
            arr2.append(line)
    n = 10000 #len(arr1)
    f.close()
    # insertion sort
    start = time.time()
    for i in range(n):
        for j in range(i+1, n):
            if arr1[i] > arr1[j]:
                arr1[i], arr1[j] = arr1[j], arr1[i]
    end = time.time()
    # print(arr1)
    print(end - start)
    
    start = time.time()
    arr3 = []
    pq = HeapQ()
    for i in range(n):
        pq.add(arr2[i], 0)
    for i in range(n):
        arr3.append(pq.remove_min())
    end = time.time()
    print(end - start)
