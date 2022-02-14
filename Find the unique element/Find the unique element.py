from sys import stdin
from collections import Counter


def findUnique(arr, n):
    result = Counter(arr)
    for key, item in result.items():
        if item == 1:
            return key


def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    print(findUnique(arr, n))

    t -= 1