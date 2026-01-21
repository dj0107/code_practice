class Node:
    def __init__(self, left, right, parent, key, value):
        self._left = left
        self._right = right
        self._parent = parent
        self._key = key
        self._value = value
        self._height = 0  # leaf 노드 height = 0
class AVLTree:
    def __init__(self):
        self._root = None
        self._size = 0
    def __len__(self):
        return self._size
    def isEmpty(self):
        return self._size == 0
    def height(self, node):
        if node is None:
            return -1
        else:
            return node._height
    def treeSearch(self, node:Node, key):
        """
        재귀적으로 키 값에 해당하는 노드를 찾음. 실패 시 마지막 노드 반환.
        """
        if key == node._key: return node
        elif key < node._key and node._left is not None:
            return self.treeSearch(node._left, key)
        elif key > node._key and node._right is not None:
            return self.treeSearch(node._right, key)
        
        return node
    def insert(self, key, value):
        # 빈 경우
        if self.isEmpty():
            self._root = Node(None, None, None, key, value)
            self._size += 1
            return # 나가기
        # 일반적 BST 삽입
        self._insert_rec(self._root, key, value)
        # trinode restructuring
    def _insert_rec(self, node:Node, key, value):
        """
        BST 삽입을 수행하는 함수. trinode restructuring은 수행하지 않음.
        return은 하지 않고 leaf까지 도달해서 삽입 수행.
        size도 증가시킴.
        """
        # 빈 트리에 넣는 경우는 insert에서 이미 예외처리함
        # 
        tnode:Node = self.treeSearch(self._root, key)

        # 키값에 해당하는 노드를 찾은 경우, 새로 추가 하지 말고 값만 바꾸고 빠져나오기
        if tnode is not None and key == tnode._key:
            tnode._value = value
            return

        # target node의 키 값과 비교해 좌 또는 우에 자식 만들어서 넣기
        if key < tnode._key:# 왼쪽 자식에 추가
            tnode._left = Node(None, None, tnode, key, value)
        else: # 오른쪽 자식에 추가
            tnode._right = Node(None, None, tnode, key, value)
        self._size += 1
    def delete(self, key):
        tnode = self.treeSearch(self._root, key)
        if tnode is None or tnode._key != key:
            raise ValueError('no element with such key')
        self._delete_node(tnode)
        self._size -= 1


    def _delete_node(self, node:Node):
        """
        노드 삭제를 수행하는 함수.
        자식이 없는 경우, 하나인 경우, 두 개인 경우
        세 가지 경우를 모두 처리.
        """
        if node._left is None and node._right is None: # 자식 없는 경우
            if node == self._root: # 루트 노드인 경우
                self._root = None
            else:
                if node == node._parent._left:
                    node._parent._left = None
                else:
                    node._parent._right = None
        elif node._left is None or node._right is None: # 자식 하나인 경우
            child = node._left if node._left is not None else node._right
            if node == self._root: # 루트 노드인 경우
                self._root = child
                child._parent = None
            else:
                if node == node._parent._left:
                    node._parent._left = child
                else:
                    node._parent._right = child
                child._parent = node._parent
        else: # 자식 두 개인 경우
            ### 가장 어려운 경우 ###
            # 왼쪽 서브트리에서 가장 큰 노드 찾기
            pred = node._left
            while pred._right is not None:
                pred = pred._right
            # 노드 교체
            node._key = pred._key
            node._value = pred._value
            # pred 노드 삭제(재귀 호출)
            # 이 때는 pred의 자식이 없거나 하나라서 이중 재귀는 없음
            self._delete_node(pred)

if __name__ == '__main__':
    bst = AVLTree()
    bst.insert(3,3)
    bst.insert(1,1)
    bst.insert(4, 4)
    bst.insert(-1, -1)

    bst.delete(3)
    print(bst._root._key)
    print(bst._root._left._key)
    print(bst._root._right._key)
    bst.delete(4)
    bst.delete(1)
    bst.delete(-1)
