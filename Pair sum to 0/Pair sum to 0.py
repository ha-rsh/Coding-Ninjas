from sys import stdin
from collections import Counter


def zero_pairs(num):
    return int(num * (num - 1) / 2)


def pairSum0(arr, size):
    count = 0
    my_dict = Counter(arr)
    if size == 1:
        return 0

    if len(my_dict) == 1 and (list(my_dict.keys())[0] == 0):
        if my_dict[0] == 2:
            return 1
        else:
            return zero_pairs(my_dict[0])
    else:
        for key, value in my_dict.items():
            if key != 0:
                new_key = key * -1
                if new_key in my_dict:
                    count = count + my_dict[key] * my_dict[new_key]
                    my_dict[new_key] = 0
                    my_dict[key] = 0
            if key == 0:
                count = count + zero_pairs(my_dict[0])
        return count


def takeInput():
    # To take fast I/O
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split()))
    return arr, n


arr, n = takeInput()
print(pairSum0(arr, n))