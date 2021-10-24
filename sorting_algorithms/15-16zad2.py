from math import log, inf

# Złożoność: O(n+lognloglogn+n) = O(n)
# lognloglogn < n dla n > 1


def partition(A, start, end):

    pivot = A[end]
    pIndex = start
    for i in range(start, end):
        if A[i] <= pivot:
            A[i], A[pIndex] = A[pIndex], A[i]
            pIndex += 1

    A[end], A[pIndex] = A[pIndex], A[end]

    return pIndex


def quicksort(A, start, end):

    while start < end:
        pivot = partition(A, start, end)
        if pivot - start < end - pivot:
            quicksort(A, start, pivot-1)
            start = pivot + 1
        else:
            quicksort(A, pivot+1, end)
            end = pivot - 1



def solve(A):
    n = len(A)
    size = int(log(n, 2))
    B = [0]*size
    j = 0

    for i in range(n):
        if A[i]%2 == 0:
            B[j] = A[i]
            A[i] = inf
            j+=1

    quicksort(B, 0, size-1)

    j = 0
    for i in range(n):
        if A[i] == inf:
            A[i] = B[j]
            j += 1

    return A




