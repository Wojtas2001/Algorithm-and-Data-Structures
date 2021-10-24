

def sortString(A):
    radixsort(A)


def radixsort(A):
    max = 0
    for i in range(len(A)):
        if max < len(A[i]):
            max = len(A[i])
    x = max
    # print(x)
    while x:
        countsort(A, x-1)
        x -= 1
    print(A)


def countsort(A, j):
    k = 27
    C = [0]*k
    B = [0]*len(A)
    for i in range(len(A)):
        if j <= len(A[i])-1:
            C[ord(A[i][j])-ord('a')+1] += 1
        else:
            C[0] += 1

    for i in range(1, k):
        C[i] += C[i-1]

    for i in range(len(A)-1, -1, -1):
        if j <= len(A[i])-1:

            C[ord(A[i][j])-ord('a')+1] -= 1
            B[C[ord(A[i][j])-ord('a')+1]] = A[i]
        else:
            C[0] -= 1
            B[C[0]] = A[i]

    for i in range(len(A)):

        A[i] = B[i]



array = ["kra", "arti", "kota", "kitx", "atiz", "kil"]
sortString(array)