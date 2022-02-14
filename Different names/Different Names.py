def differentNames(l):
    my_dict = {}
    for i in l:
        my_dict[i] = my_dict.get(i, 0) + 1

    for key, item in my_dict.items():
        if item > 1:
            print(key, item)

    if len(l) == len(my_dict) or len(l) == 0:
        print(-1)


names = input().strip().split()
differentNames(names)