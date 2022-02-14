def lastIndex(arr, x, n):
    if n < 0:
        return -1
    if arr[n - 1] == x:
        return n - 1
    return lastIndex(arr, x, n - 1)


from sys import setrecursionlimit

setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
print(lastIndex(arr, x, n))