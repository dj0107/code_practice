import time
import random
import sys
sys.setrecursionlimit(999999)
INF = float('inf')

def isSorted(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i-1]: return False
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
    
def quickSort(arr):
    pass

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

    # insertion sort
    start = time.time()
    print(isSorted(arr1))
    insertionSort(arr1)
    print(isSorted(arr1))
    print("elapsed time:", time.time() - start)

    # selection sort
    start = time.time()
    print(isSorted(arr2))
    selectionSort(arr2)
    print(isSorted(arr2))
    print("elapsed time:", time.time() - start)

    # merge sort
    start = time.time()
    print(isSorted(arr3))
    mergeSort(arr3)
    print(isSorted(arr3))
    print("elapsed time:", time.time() - start)



    
