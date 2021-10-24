

def partiton(A, start, end):

    pivot = A[end]
    pIndex = start
    for i in range(start, end):
        if A[i] <= pivot:
            A[i], A[pIndex] = A[pIndex], A[i]
            pIndex += 1

    A[pIndex], A[end] = A[end], A[pIndex]
    return pIndex


def quicksort(A, start, end):

    while start < end:
        pivot = partiton(A, start, end)
        if pivot - start < end - pivot:
            quicksort(A, start, pivot-1)
            start = pivot + 1
        else:
            quicksort(A, pivot+1, end)
            end = pivot - 1




def solve(T, x):
    quicksort(T, 0, len(T)-1)
    print(T)
    i = 0
    j = len(T)-1

    while i < j:
        if T[i]+T[j] == x:
            print(T[i], T[j])
            return True
        elif T[i]+T[j] > x:
            j -= 1
        else:
            i += 1

    return False


tab = [1, 3, 6, 2, 9, 10, 2, 2, 11]
print(solve(tab, 10))