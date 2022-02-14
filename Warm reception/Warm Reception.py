def min_chair(arrival_time, departure_time, size):
    arrival_time.sort()
    departure_time.sort()
    chair_needed = 1
    result = 1
    i = 1
    j = 0

    while (i < size and j < size):
        if (arrival_time[i] <= departure_time[j]):
            chair_needed += 1
            i += 1

        elif (arrival_time[i] > departure_time[j]):
            chair_needed -= 1
            j += 1

        if (chair_needed > result):
            result = chair_needed

    return result


size = int(input())
arrival_time = list(int(i) for i in input().strip().split(' '))
departure_time = list(int(i) for i in input().strip().split(' '))
print(min_chair(arrival_time, departure_time, size))