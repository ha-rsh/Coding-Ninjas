from sys import stdin
from collections import Counter


def findDuplicate(arr, n):
    result = Counter(arr)
    for key, item in result.items():
        if item == 2:
            return key


def takeInput():
    n = int(stdin.readline().rstrip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


t = int(stdin.readline().rstrip())

while t > 0:
    arr, n = takeInput()
    print(findDuplicate(arr, n))

    t -= 1