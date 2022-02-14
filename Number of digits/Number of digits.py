c = 0


def count(num):
    global c
    if num != 0:
        c += 1
        count(num // 10)
    return c


n = int(input())
print(count(n))