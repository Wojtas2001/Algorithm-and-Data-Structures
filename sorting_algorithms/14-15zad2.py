class Node:
    def __init__(self):
        self.value = None
        self.next = None

class TwoLists:
    def __init__(self):
        self.even = Node()
        self.odd = Node()


def TwoLists_split(L):

    res_List = TwoLists()
    head_even = res_List.even
    head_odd = res_List.odd

    while L != None:

        if L.value%2 == 0:
            res_List.even.next = L
            # print(res_List.even.value)

            res_List.even = res_List.even.next
        else:
            res_List.odd.next = L
            res_List.odd = res_List.odd.next

        L = L.next

    res_List.even = head_even
    res_List.odd = head_odd
    return res_List

def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X

    return H.next

tab = [2, 1 ,3, 7, 5, 5, 9, 10, 13, 12]
x = tab2list(tab)
list = TwoLists_split(x)
list.even = list.even.next
list.odd = list.odd.next
print('Even:')
while list.even != None:
    print(list.even.value, end=" ")
    list.even = list.even.next
print()
print('Odd:')
while list.odd != None:
    print(list.odd.value, end=" ")
    list.odd = list.odd.next