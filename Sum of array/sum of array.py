from sys import setrecursionlimit
setrecursionlimit(11000)


def sumArray(arr,n):
    if n == 0:
        return 0
    else:
        return arr[n-1]+sumArray(arr,n-1)


n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
print(sumArray(arr, n))
