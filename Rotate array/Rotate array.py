from sys import stdin


def rotate(arr, size, d):
    my_list = []
    list_1 = []
    list_2 = []
    if size > 1:
        temp = arr[size - 1]
    else:
        return
    arr.insert(d, 'x')
    for i in range(size - 1):
        if i < d:
            list_1.append(arr[i])

        else:
            list_2.append(arr[i + 1])

    list_2.append(temp)

    for i in list_2:
        my_list.append(i)

    for i in list_1:
        my_list.append(i)

    return my_list


def takeInput():
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


t = int(stdin.readline().rstrip())

while t > 0:
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    new_arr = rotate(arr, n, d)
    printList(new_arr, n)

    t -= 1