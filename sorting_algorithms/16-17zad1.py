from math import floor


class Node:
    def __init__(self):
        self.value = None
        self.next = None



def selectionSort(head):

    a = head
    b = head

    while b.next != None:
        c = b.next
        d = b.next

        while d != None:

            if b.value > d.value:
                # if d znajduje sie odrazu za b
                if b.next == d:

                    if b == head:

                        b.next = d.next
                        d.next = b

                        b, d = d, b
                        c = d
                        head = b
                        d = d.next
                    else:
                        b.next = d.next
                        d.next = b
                        a.next = d
                        b, d = d, b
                        c = d
                        d = d.next
                else:
                    if b == head:
                        r = b.next
                        b.next = d.next
                        d.next = r
                        c.next = b

                        b, d = d, b

                        c = d

                        d = d.next

                        head = b
                    else:
                        r = b.next
                        b.next = d.next
                        d.next = r
                        c.next = b
                        a.next = d
                        b, d = d, b
                        c = d
                        d = d.next
            else:
                c = d
                d = d.next

        a= b
        b = b.next

    return head




def sortList(L):

    head = L
    n = 0
    while L != None:
        n += 1
        L = L.next

    L = head
    buckets = [Node() for _ in range(n)]

    heads_buc = [0]*n
    for i in range(n):
        heads_buc[i] = buckets[i]


    for _ in range(n):

        b = L.value
        buckets[floor(b/4*n)].next = L
        buckets[floor(b/4*n)] = buckets[floor(b/4*n)].next
        L = L.next

    for i in range(n):
        buckets[i].next = None
        if heads_buc[i].next != None:
            selectionSort(heads_buc[i].next)

    sorted_list = Node()
    head_s = sorted_list
    for i in range(n):
        heads_buc[i] = heads_buc[i].next
        while heads_buc[i] != None:
            sorted_list.next = heads_buc[i]
            heads_buc[i] = heads_buc[i].next
            sorted_list = sorted_list.next

    head_s = head_s.next
    while head_s != None:
        print(head_s.value)
        head_s = head_s.next



def tabToList(x):

    start = Node()
    start.value = x[0]
    curr = start

    for i in range(1, len(x)):
        curr.next = Node()
        curr.next.value = x[i]
        curr = curr.next

    return start



test = [2, 2, 2.40, 2, 2, 3, 3, 1]
t = tabToList(test)
sortList(t)