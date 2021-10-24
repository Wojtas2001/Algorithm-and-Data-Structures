from typing import Any, Iterator
from collections.abc import Sequence
import math


class Linear_2D_array(Sequence):
    """
    Abstraction layer that allows using 2D array of size NxN like 1D array of size N^2.
    Input array is mapped to areas A, B and C like this:
    +-------------+
    | B1 C6 C5 C3 |
    | A1 B2 C4 C2 |
    | A2 A3 B3 C1 |
    | A4 A5 A6 B4 |
    +-------------+
    is mapped to
    [A1...A6|B1...B4|C1...C6]
    """

    def __init__(self, array) -> None:
        self.array = array
        self.size = len(array)

    @staticmethod
    def get_index_groupA(i: int) -> tuple[int, int]:
        """
        Converts i index in a flat array to x and y in 2D quadratic array (only in group A)
        """

        # solve 1+2+3+...+y >= i+1 for the smallest natural y
        # in rows 1, 2, 3, ..., y is enough cells for i-th smallest elelent to fit in
        y = math.ceil((math.sqrt(9 + 8 * i) - 1) / 2)

        if y * (y - 1) // 2 >= i + 1:  # (never gonna happen (I think so, at least))
            print("reduced")
            y -= 1

        earlier = y * (y - 1) // 2  # How many cells are earlier
        x = i - earlier

        return x, y

    def get_index(self, i: int) -> tuple[int, int]:
        if self.size == 1:
            if i > 0:
                raise IndexError
            return 0, 0

        AC_areas_len = (self.size ** 2 - self.size) // 2
        if i >= AC_areas_len and i < AC_areas_len + self.size:
            idx = i - AC_areas_len
            return idx, idx

        if i < AC_areas_len:
            return Linear_2D_array.get_index_groupA(i)

        # weird hack
        y, x = Linear_2D_array.get_index_groupA(self.size ** 2 - i - 1)
        return x, y

    def __len__(self) -> int:
        return self.size ** 2

    def __getitem__(self, i: int) -> Any:
        x, y = self.get_index(i)
        return self.array[y][x]

    def __setitem__(self, i: int, val: Any) -> None:
        x, y = self.get_index(i)
        self.array[y][x] = val

    def __iter__(self) -> Iterator:
        self.i = 0
        return self

    def __next__(self) -> Any:
        if self.i >= self.size ** 2:
            raise StopIteration

        val = self[self.i]
        self.i += 1
        return val

    def __str__(self) -> str:
        return str([self[i] for i in range(len(self))])





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






import copy

T1 = [ [1,2], [3,4] ]
T2 = [ [2,3,5], [7,11,13], [17,19,23] ]
T3 = [ [2, 5, 2, 5], [2, 5, 5, 2],[2, 5, 2, 2],[2, 5, 5, 5] ]
T4 = [ [43, 74, 53, 97], [80, 61, 61, 19], [61, 73, 89, 93], [42, 17, 89, 80] ]

TESTS = [ T1, T2, T3, T4 ]


def isok(T):
  N = len(T)
  for r in range(1,N):
    for c in range(r):
      for d in range(N):
        if T[r][c]>T[d][d]: return False
        if T[c][r]<T[d][d]: return False
  return True

def printT(T):
  N = len(T)
  for row in T: print(row)
  print()



def runtests(f):
    OK = True
    for T in TESTS:
        print("----------------------")
        print("Dane:")
        printT(T)
        f(T)
        print("Wynik:")
        printT(T)

        if not isok(T):
            print("Blad!")
            OK = False
    print("----------------------")

    if OK:
        print("OK!")
    else:
        print("Bledy!")

def solve(T):
    arr = Linear_2D_array(T)
    quickselect(arr, 0, len(arr)-1, (len(T)**2-len(T))//2)
    quickselect(arr, (len(T)**2-len(T))//2, len(arr)-1, (len(T)**2-len(T))//2+len(T))

    return T




if __name__ == "__main__":
    arr = [
        [6, 15, 14, 12],
        [0, 7, 13, 11],
        [1, 2, 8, 10],
        [3, 4, 5, 9]
    ]
    #
    # arr2 = [
    #     [2, 3, 5],
    #     [7, 11, 13],
    #     [17, 19, 23],
    # ]
    # test2 = Linear_2D_array(arr2)
    # print(test2)
    #
    # quickselect(test2, 0, len(test2)-1, (len(arr2)**2-len(arr2))//2)
    # quickselect(test2, 2, len(test2)-1, (len(arr2)**2-len(arr2))//2+len(arr2))

    # for el in arr2:
    #     print(el)
    # print()

    runtests(solve)



    """
    test = Linear_2D_array(arr)
    print(test)
    for el in arr:
        print(el)
    print()
    for i in range(len(test)):
        print(test[i], end=" ")
    print("after i")
    for el in test:
        print(el, end=" ")
    print()"""