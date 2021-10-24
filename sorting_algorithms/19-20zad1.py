
def preprocessing(T):

    # ladna_tab = [False]*10
    # nieladna_tab = [False]*10
    occur = [0 ] *10
    ladna = 0
    nieladna = 0

    for i in range(len(T)):
        temp = T[i]
        while temp > 0:
            occur[temp % 10] += 1
            temp //= 10

        for j in range(len(occur)):
            if occur[j] == 1:
                ladna += 1
            elif occur[j] > 1:
                nieladna += 1


            occur[j] = 0

        T[i] = (ladna, nieladna, T[i])
        ladna = 0
        nieladna = 0

    return T


def countSort(A, j):
    k = 10
    C = [0] *k
    B = [0] *len(A)
    for i in range(len(A)):
        C[A[i][j]] += 1

    for i in range(1, k):
        C[i] += C[i-1]

    for i in range(len(A)-1, -1, -1):
        C[A[i][j]] -= 1
        B[C[A[i][j]]] = A[i]


    for i in range(len(A)):
        A[i] = B[i]



def pretty_sort(T):

    T = preprocessing(T)
    countSort(T, 1)
    for i in range(len(T)//2):
        T[i], T[len(T)-1-i] = T[len(T)-1-i], T[i]

    countSort(T, 0)

    for i in range(len(T)//2):
        T[i], T[len(T)-1-i] = T[len(T)-1-i], T[i]

    for i in range(len(T)):
        T[i] = T[i][2]

    return T


# Na przykład: liczba 123 jest ładniejsza od
# 455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333

print(pretty_sort([123, 455, 1266, 114577, 2344, 67333]))
# print(preprocessing([123, 123112, 998, 887]))