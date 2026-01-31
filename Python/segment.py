class Node:
    def __init__(self, left, right, start, end, val):
        self._left = left
        self._right = right
        self._start = start
        self._end = end
        self._val = val

class segTree:# 한번에 배열을 받고, insert/delete는 없다고 가정
    def __init__(self, arr):
        self._n = len(arr)
        


