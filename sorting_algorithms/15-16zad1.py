

# złożoność: O(n^2)

def partiton(A, start, end):

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
        pivot = partiton(A, start, end)
        if pivot - start < end - pivot:
            quicksort(A, start, pivot-1)
            start = pivot+1
        else:
            quicksort(A, pivot+1, end)
            end = pivot - 1




def sumSort(A, B, n):

    sums = [0]*n
    for i in range(n):
        for j in range(n):
            sums[i] += A[i][j]

    for i in range(n):
        sums[i] = (sums[i], i)

    quicksort(sums, 0, n-1)

    for i in range(n):
        for j in range(n):
            B[i][j] = A[sums[i][1]][j]


    # for el in A:
    #     print(el)
    # print()
    # for el in B:
    #     print(el)

    return B

array = [
    [2, 7, 1, 9],
    [3, 6, 1 ,2],
    [3, 9, 1 ,7],
    [6, 9 ,1, 6]
         ]
arr2 = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

sumSort(array, arr2, len(array))
