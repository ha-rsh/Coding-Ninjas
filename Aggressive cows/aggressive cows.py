from sys import stdin

def max_distance(mid, arr, cows, size):
    c = 1
    pos = arr[0]
    for i in range(1, size):
        if arr[i] - pos >= mid:
            pos = arr[i]
            c += 1
            if c == cows:
                return 1
            
    return 0

def binarysearch(arr, size, cows):
    beg = 0
    end = arr[size-1]
    max = -1
    while end > beg:
        mid = beg + (end-beg)//2
        if max_distance(mid, arr, cows, size) == 1:
            if mid > max:
                max = mid   
            beg = mid + 1
            
        else:
            end = mid
            
    return int(max)
            
def takeInput() :
    value = list(map(int, stdin.readline().strip().split(" ")))
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, value


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()

t = int(stdin.readline().strip())

while t > 0 :
    
    arr, value = takeInput()
    arr.sort()
    size = value[0]
    cows = value[1]
    print(binarysearch(arr, size, cows))

    t -= 1