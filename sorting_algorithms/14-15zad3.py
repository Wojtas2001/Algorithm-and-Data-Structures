

def binarySearch(array, x, index):
    left, right = (0, index-1)
    while left <= right:
        mid = (left+right)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            left = mid+1
        else:
            right = mid-1
    return -1



def find(T): # funkcja ta tworzy posortowaną tablice bez powtórzeń
    n = len(T)
    new_T = [0]*n
    index = 0
    for i in range(len(T)):
        if binarySearch(new_T, T[i], index) == -1:
            j = index-1
            while j >= 0 and new_T[j] > T[i]:
                new_T[j+1] = new_T[j]
                j -= 1
            new_T[j+1] = T[i]
            index += 1

    new_T2 = [0]*index
    for i in range(index):
        new_T2[i] = new_T[i]


    return new_T2, index


def sort(T):
    n = len(T)
    arr, n2 = find(T)

    C = [0]*n2
    B = [0]*n

    for i in range(len(T)):
        C[binarySearch(arr, T[i], n2)] += 1

    for i in range(1, n2):
        C[i] += C[i-1]

    for i in range(len(T)-1, -1, -1):
        C[binarySearch(arr, T[i], n2)] -= 1
        B[C[binarySearch(arr, T[i], n2)]] = T[i]

    for i in range(len(T)):
        T[i] = B[i]

    print(T)
    return T


A = [1, 2, 3, 1, 2, 3, 1, 2]
sort(A)