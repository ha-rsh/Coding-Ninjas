def uniqueChar(string):
    my_list = []
    for i in range(len(string)):
        c = string[i]

        if c not in my_list:
            my_list.append(c)

    return "".join(my_list)


string = input()
print(uniqueChar(string))