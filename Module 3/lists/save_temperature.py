from random import random

def random_temp(min, max):
    temp = min + (max-min) * random()
    return temp

temps = [[random_temp(15, 30) for h in range(24)] for d in range(31)]

total = 0.

for day in temps:
    total += day[11]

average = total/31

print('Average midday temperature: ', average)

highest = 0.

for day in temps:
    for hour in day:
        if hour > highest:
            highest = hour

print(highest)

count_min_20 = 0
limit = 20

for day in temps:
    if day[11] > limit:
        count_min_20 += 1

print('Amount of noons above 20: ', count_min_20)
