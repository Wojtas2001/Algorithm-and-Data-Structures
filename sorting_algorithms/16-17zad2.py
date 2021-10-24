


def partition(A, start, end):

    pivot = A[end]
    pIndex = start
    for i in range(start, end):
        if A[i] <= pivot:
            A[i], A[pIndex] = A[pIndex], A[i]
            pIndex += 1

    A[end], A[pIndex] = A[pIndex], A[end]
    return pIndex


def quickselect(A, start, end, k):

    if start == end:
        return A[start]

    pIndex = partition(A, start, end)

    if k == pIndex:
        return A[k]

    elif k < pIndex:
        return quickselect(A, start, pIndex-1, k)

    else:
        return quickselect(A, pIndex+1, end, k)




def sumBetween(T, start, end):

    quickselect(T, 0, len(T)-1, start)
    quickselect(T, start, len(T)-1, end)
    res = 0
    for i in range(start, end):
        res += T[i]

    print(T)
    return res


A = [10, 2, 6, 1, 7, 18, 4, 8, 12, 14]
print(A)
print(sumBetween(A, 2, 5))
