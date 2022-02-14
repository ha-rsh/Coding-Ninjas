from sys import stdin

def replace_character(my_list, replace, replace_with):
    for i in range(len(my_list)):
        if my_list[i] == replace:
            my_list[i] = replace_with
        print(my_list[i], end="")
        
    print("")

t = int(stdin.readline().strip())

while t > 0 :
    str = input()
    str_2 = input()
    replace = str_2[0]
    replace_with = str_2[2]
    str.strip()
    my_list = list(str)
    replace_character(my_list, replace, replace_with)

    t -= 1