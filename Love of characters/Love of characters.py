s = input()
c = input()
dict = {}

for i in c:
    dict[i] = dict.get(i, 0) + 1

if 'a' in c:
    print(dict['a'], end=" ")
else:
    print('0', end=" ")

if 's' in c:
    print(dict['s'], end=" ")
else:
    print('0', end=" ")

if 'p' in c:
    print(dict['p'], end=" ")
else:
    print('0', end=" ")