



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


def section(T, p, q):

    ans = [0]*(q-p+1)
    quickselect(T, 0, len(T)-1, p)
    quickselect(T, p, len(T)-1, q)
    for i in range(len(ans)):
        ans[i] = T[p+i]
    print(ans)


tab = [2, 6, 1, 999, 213, 999, 13, 4, 3, 3, 10, 12, 8, 9, 2, 2, 1, 159, 213, 19, 2, 6, 8, 5, 49, 9, 99]
section(tab, 6, 8)
tab.sort()
print(tab)