def allIndex(arr, x, start):
    if start == len(arr):
        ans = []
        return ans

    Index = allIndex(arr, x, start + 1)

    if arr[start] == x:
        myAns = [0 for i in range(len(Index) + 1)]

        myAns[0] = start
        for i in range(len(Index)):
            myAns[i + 1] = Index[i]

        return myAns
    else:

        return Index


from sys import setrecursionlimit

setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())

output = allIndex(arr, x, 0)

for i in output:
    print(i, end=" ")