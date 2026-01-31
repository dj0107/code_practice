import time
import random
import sys
from collections import deque
sys.setrecursionlimit(999999)
INF = float('inf')

def isSorted(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i-1]: 
            print(arr[i-1], "in front of", arr[i])
            return False
    return True

def insertionSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        minVal = INF
        for j in range(i, n):
            if arr[j] < minVal:
                minVal = arr[j]
                idx = j
        
        arr[i], arr[idx] = arr[idx], arr[i]

def mergeSort(arr):
    n = len(arr)
    if n < 2: return
    mid = n // 2
    arr1 = arr[:mid]
    arr2 = arr[mid:]
    mergeSort(arr1)
    mergeSort(arr2)

    merge(arr1, arr2, arr)

def merge(arr1, arr2, arr):
    
    n1 = len(arr1)
    n2 = len(arr2)
    left, right = 0, 0
    while left + right < n1 + n2:
        if (left == n1) or (right != n2 and arr1[left] >= arr2[right]):
            arr[left + right] = arr2[right]
            right += 1
        else:
            arr[left + right] = arr1[left]
            left += 1
    
def radixSort(arr, d):
    """
    자릿수 d인 정수에 대해 radix sort.
    """
    
    for i in range(d):
        darr = [deque() for _ in range(10)]
        to_divide = 10 ** i
        for j in range(len(arr)):
            idx = (arr[j] % (10 * to_divide)) // to_divide
            darr[idx].append(arr[j])
        arr.clear()
        for j in range(10):
            while darr[j]:
                arr.append(darr[j].popleft())
        
        


# def infLoop(n):
#     print(n)
#     infLoop(n+1)
    

if __name__ == '__main__':
    arr1 = []
    f = open('sorttest.txt', 'r')
    for line in f:
        arr1.append(int(line))
    f.close()
    arr1 = arr1[:10000]
    arr2 = arr1[:]
    arr3 = arr1[:]
    arr4 = arr1[:]
    d = 0
    for val in arr1:
        d = max(d, val)
    print(f"biggest one: {d}")
    d = len(str(d))

    # # insertion sort
    # start = time.time()
    # print(isSorted(arr1))
    # insertionSort(arr1)
    # print(isSorted(arr1))
    # print("elapsed time:", time.time() - start)

    # # selection sort
    # start = time.time()
    # print(isSorted(arr2))
    # selectionSort(arr2)
    # print(isSorted(arr2))
    # print("elapsed time:", time.time() - start)

    # merge sort
    start = time.time()
    print(isSorted(arr3))
    mergeSort(arr3)
    print(isSorted(arr3))
    print("elapsed time:", time.time() - start)

    # radix sort
    start = time.time()
    print(isSorted(arr4))
    radixSort(arr4, d)
    print(isSorted(arr4))
    # print(arr4)
    print("elapsed time:", time.time() - start)



    
