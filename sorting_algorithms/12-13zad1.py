from random import randint, seed



class Node:
    def __init__(self):
        self.next = None
        self.value = None


def partition(start, end):


    less_than_pivot = Node()
    greater_than_pivot = Node()
    equal_pivot = Node()

    less_than_pivot_head = less_than_pivot
    greater_than_pivot_head = greater_than_pivot
    equal_pivot_head = equal_pivot

    equal_pivot.next = start.next # wybieram pivot jako pierwszy element
    equal_pivot = equal_pivot.next
    curr = start.next.next

    greater_l = 0
    less_l = 0

    while curr != end:
        if curr.value == equal_pivot.value:
            equal_pivot.next = curr
            equal_pivot = equal_pivot.next

        elif curr.value < equal_pivot.value:
            less_than_pivot.next = curr
            less_than_pivot = less_than_pivot.next
            less_l += 1

        else:
            greater_than_pivot.next = curr
            greater_than_pivot = greater_than_pivot.next
            greater_l += 1

        curr = curr.next

    greater_than_pivot.next = end
    equal_pivot.next = greater_than_pivot_head.next
    less_than_pivot.next = equal_pivot_head.next
    start.next = less_than_pivot_head.next


    return equal_pivot_head.next, equal_pivot, less_l, greater_l


def quicksort(start, end):

    while start.next != end:
        pivot_start, pivot_end, smaller_l, greater_l = partition(start, end)

        if smaller_l > greater_l:
            quicksort(pivot_end, end)
            end = pivot_start
        else:
            quicksort(start, pivot_start)
            start = pivot_end



def qsort(L):
    head = Node()
    head.next = L
    quicksort(head, None)
    return head.next


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next



def printlist(L):
    while L != None:
        print(L.value, "->", end=" ")
        L = L.next
    print("|")


seed(42)

n = 10
T = [randint(1, 10) for i in range(10)]
L = tab2list(T)

print("przed sortowaniem: L =", end=" ")
printlist(L)
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
    print("List jest pusta, a nie powinna!")
    exit(0)

P = L
while P.next != None:
    if P.value > P.next.value:
        print("Błąd sortowania")
        exit(0)
    P = P.next

print("OK")
