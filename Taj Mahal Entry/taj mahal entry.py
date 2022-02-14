from sys import stdin

def entry(arr, n):
    my_list = []
    for i in range(n):
        if arr[i] <= i:
            my_list.append(i)
            
        else:
            my_list.append((n+i+(arr[i]//n)))
            
    index = 0
    for i in range(n):
        if my_list[index] > my_list[i]:
            index = i
            
    print(index+1)
            

def takeInput() :
    size = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, size

    
arr, size = takeInput()
entry(arr, size)