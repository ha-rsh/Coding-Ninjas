from sys import stdin

def skillsort(arr, start, end, size):
    for i in range(size-1):
        if arr[i] > arr[i+1]:
            if arr[i] - arr[i+1] > 1:
                return 0
            elif arr[i] - arr[i+1] == 1:
                t=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=t
    return 1

def takeInput() :
    size = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, size

t = int(stdin.readline().strip())

while t > 0 :
    
    arr, size = takeInput()
    if skillsort(arr, 0, size-1, size) == 1:
        print('Yes')
    else:
        print('No')

    t -= 1