from sys import setrecursionlimit
setrecursionlimit(11000)


def numbers(n):
    if n <= 0:
        return
    numbers(n - 1)
    print(n, end=" ")


n = int(input())
numbers(n)