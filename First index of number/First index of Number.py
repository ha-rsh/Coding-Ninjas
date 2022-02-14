def firstIndex(arr, x, n):
    if n == 1 and arr[0] == x:
        return 0
    elif x not in arr:
        return -1
    elif arr[n - 1] == x:
        return arr.index(x)
    else:
        return firstIndex(arr, x, n - 1)


from sys import setrecursionlimit
setrecursionlimit(11000)

n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
print(firstIndex(arr, x, n))