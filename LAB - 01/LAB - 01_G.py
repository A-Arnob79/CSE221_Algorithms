num = int(input())
sorted_trains = []

for i in range(num):
    s = input().split(' ')
    train_name = s[0]
    des = s[4]
    dep = s[-1]
    sorted_trains.append([train_name, des, dep, i])

def time_calc(x):
    h, m = x.split(':')
    return int(h) * 60 + int(m)


for i in range(num):
    for j in range(num - i - 1):

        if sorted_trains[j][0] > sorted_trains[j + 1][0]:
            sorted_trains[j], sorted_trains[j + 1] = sorted_trains[j + 1], sorted_trains[j]
        elif sorted_trains[j][0] == sorted_trains[j + 1][0]:

            if time_calc(sorted_trains[j][2]) < time_calc(sorted_trains[j + 1][2]):
                sorted_trains[j], sorted_trains[j + 1] = sorted_trains[j + 1], sorted_trains[j]

            elif time_calc(sorted_trains[j][2]) == time_calc(sorted_trains[j + 1][2]):
                if sorted_trains[j][3] > sorted_trains[j + 1][3]:
                    sorted_trains[j], sorted_trains[j + 1] = sorted_trains[j + 1], sorted_trains[j]

for t in sorted_trains:
    print(f'{t[0]} will departure for {t[1]} at {t[2]}')