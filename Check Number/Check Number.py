from sys import setrecursionlimit
setrecursionlimit(11000)


def checkNumber(arr, x, n):
    # Please add your code here
    if n == 0:
        return
    elif arr[n-1] == x:
        return True
    else:
        return checkNumber(arr, x, n-1)


n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
if checkNumber(arr, x, n):
    print('true')
else:
    print('false')