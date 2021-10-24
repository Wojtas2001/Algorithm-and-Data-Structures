
# Struktura pozwalająca w czasie O(logn), usunąć minimum
# jak i maksimum. Struktura polega na zbudowaniu dwóch kopców binarnych
# min i max. Jedyny problem w tej strukturze to usuwanie elementów
# gdy usuniemy min w kopcu chcemy je usunąc również w kopcu max.
# Rozwiazaniem tego problemu jest stworzenie listy w której oprócz wartości
# jaką mamy przechowujemy również indeksy danej wartości w min jak i max kopcu.
# A więc usunięcie z kopca min jak i max zajmuje log(n)
# a znalezienie w liście max i minimum to O(1) ponieważ wskaźnik na tego
# Noda trzymam w minheapie(maxheapie) pod indeksem 0



class Node:
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None
        self.min_index = None
        self.max_index = None


class minHeapStruct:
    def __init__(self):
        self.size = 0
        self.capacity = 10*9
        self.array = [Node()]*self.capacity


class maxHeapStruct:
    def __init__(self):
        self.size = 0
        self.capacity = 10*9
        self.array = [Node()]*self.capacity


def left(i:int):
    return 2*i+1


def right(i:int):
    return 2*i+2

def parent(i:int):
    return (i-1)//2


# def heapify_min(A:list, n:int, i:int):
#     m = i
#     l = left(i)
#     r = right(i)
#     if l < n and A[l].value < A[m].value: m = l
#     if r < n and A[r].value < A[m].value: m = r
#     if m != i:
#         A[i], A[m] = A[m], A[i]
#         heapify_min(A, n, m)


# def heapify_max(A:list, n:int, i:int):
#     m = i
#     l = left(i)
#     r = right(i)
#     if l < n and A[l].value > A[m].value: m = l
#     if r < n and A[r].value > A[m].value: m = r
#     if m != i:
#         A[i], A[m] = A[m], A[i]
#         heapify_max(A, n, m)


# def buildheap(A:list):
#     n = len(A)
#     min_heap = A
#     max_heap = A.copy()
#     for i in range(parent(n-1), -1 ,-1):
#         heapify_min(min_heap, n, i)
#         heapify_max(max_heap, n, i)
#
#     return min_heap, max_heap



# def tab2List(A:list):
#
#     head = Node()
#     head.value = A[0]
#     prev = head
#     for i in range(1, len(A)):
#         curr = Node()
#         curr.value = A[i]
#         prev.next = curr
#         prev = curr
#
#     return head


def insertMinHeap(minHeap:minHeapStruct, temp:Node):

    minHeap.size += 1
    i = minHeap.size - 1
    while i and temp.value < minHeap.array[(i-1)//2].value:
        minHeap.array[i] = minHeap.array[(i-1)//2]
        minHeap.array[i].min_index = i
        i = (i-1)//2

    minHeap.array[i] = temp
    minHeap.array[i].min_index = i


def insertMaxHeap(maxHeap:maxHeapStruct, temp:Node):

    maxHeap.size += 1
    i = maxHeap.size - 1
    while i and temp.value > maxHeap.array[(i-1)//2].value:
        maxHeap.array[i] = maxHeap.array[(i-1)//2]
        maxHeap.array[i].max_index = i
        i = (i-1)//2

    maxHeap.array[i] = temp
    maxHeap.array[i].max_index = i


def insertAtHead(list:Node, temp:Node):

    if list == None:
        list = temp


    else:
        temp.next = list
        list.prev = temp
        list = temp

    return list


class myDS:
    def __init__(self):
        self.minHeap = minHeapStruct()
        self.maxHeap = maxHeapStruct()
        self.list = None




def insertValue(myDS:myDS, value2:int):
    x = Node()
    x.value = value2
    myDS.list = insertAtHead(myDS.list, x)
    insertMaxHeap(myDS.maxHeap, x)
    insertMinHeap(myDS.minHeap, x)


def maxHeapify(maxHeap: maxHeapStruct, index:int):
    m = index
    l = left(index)
    r = right(index)
    if maxHeap.array[l] and l < maxHeap.size and maxHeap.array[l].value > maxHeap.array[m].value:
        m = l
    if maxHeap.array[r] and r < maxHeap.size and maxHeap.array[r].value > maxHeap.array[m].value:
        m = r

    if m != index:
        maxHeap.array[m].max_index, maxHeap.array[index].max_index = maxHeap.array[index].max_index, maxHeap.array[m].max_index
        maxHeap.array[m], maxHeap.array[index] = maxHeap.array[index], maxHeap.array[m]


        maxHeapify(maxHeap, m)


def minHeapify(minHeap: minHeapStruct, index: int):
    m = index
    l = left(index)
    r = right(index)
    if minHeap.array[l] and l < minHeap.size and minHeap.array[l].value < minHeap.array[m].value:
        m = l
    if minHeap.array[r] and r < minHeap.size and minHeap.array[r].value < minHeap.array[m].value:
        m = r

    if m != index:
        minHeap.array[m].min_index, minHeap.array[index].min_index = minHeap.array[index].min_index, minHeap.array[m].min_index
        minHeap.array[m], minHeap.array[index] = minHeap.array[index], minHeap.array[m]

        minHeapify(minHeap, m)


def hasOnlyOneNode(list):
    if list.next == None and list.prev == None:
       return True
    return False


def removeNode(list, temp):

    if hasOnlyOneNode(list):
        list = None


    elif temp.prev == None:
        list = temp.next
        temp.next.prev = None


    else:
        temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev

    return list


def deleteMax(myDS:myDS):


    temp = myDS.maxHeap.array[0]


    myDS.maxHeap.array[0] = myDS.maxHeap.array[myDS.maxHeap.size-1]
    myDS.maxHeap.size -= 1
    myDS.maxHeap.array[0].max_index = 0
    maxHeapify(myDS.maxHeap, 0)


    myDS.minHeap.array[temp.min_index] = myDS.minHeap.array[myDS.minHeap.size-1]
    myDS.minHeap.size -= 1
    myDS.minHeap.array[temp.min_index].min_index = temp.min_index
    minHeapify(myDS.minHeap, temp.min_index)

    myDS.list = removeNode(myDS.list, temp)


def deleteMin(myDS:myDS):


    temp = myDS.minHeap.array[0]


    myDS.minHeap.array[0] = myDS.minHeap.array[myDS.minHeap.size-1]
    myDS.minHeap.size -= 1
    myDS.minHeap.array[0].min_index = 0
    minHeapify(myDS.minHeap, 0)


    myDS.maxHeap.array[temp.max_index] = myDS.maxHeap.array[myDS.maxHeap.size-1]
    myDS.maxHeap.size -= 1
    myDS.maxHeap.array[temp.max_index].max_index = temp.max_index
    maxHeapify(myDS.maxHeap, temp.max_index)

    myDS.list = removeNode(myDS.list, temp)
    myDS.minHeap.array[0] = Node()


if __name__ == '__main__':
    A = [9, 2 ,1, 6, 10]
    # x, y = buildheap(A)
    a = myDS()
    for i in range(len(A)):
        insertValue(a, A[i])


    # deleteMin(a)
    deleteMax(a)

    while a.list != None:
        print(a.list.value, a.list.min_index, a.list.max_index)
        a.list = a.list.next

    # b = tab2List(A)

