from sys import stdin

def distribute_candies(candies, arr, students, size):
  for i in range(size):
    students -= (arr[i] // candies)
    
  if students <= 0:
    return 1
  return 0

def binarysearch(arr, size, students):
    beg = 0
    end = max(arr)
    maximum = 0
    if students == 1:
        return end
    while end >= beg:
        mid = beg + (end-beg)//2
        if distribute_candies(mid, arr, students, size) == 1:
            if mid > maximum:
                maximum = mid   
            beg = mid + 1
            
        else:
            end = mid-1
            
    return int(maximum)
            
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
    size = value[0]
    students = value[1]
    print(binarysearch(arr, size, students))

    t -= 1