from sys import stdin
from collections import Counter


arr = []
for line in stdin:
    if line != '\n':
        arr = list(map(int, line.split(',')))

print(arr)
days = [0 for i in range(9)]
for i in range(len(arr)):
    days[arr[i]] += 1
total = 0

print(days)
for _ in range(1, 257):
    new_day = [0 for i in range(9)]
    for i in range(len(days)):
        if i == 0:
            new_day[6] = days[i]
            new_day[8] = days[i]

            total += days[i]

        else:
            new_day[i-1] += days[i]

    days = [x for x in new_day]      
    # print(days)      


print(sum(days))



