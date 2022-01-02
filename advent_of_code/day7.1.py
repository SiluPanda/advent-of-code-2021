from sys import stdin

arr = []
for line in stdin:
    if line != '\n':
        arr = list(map(int, line.split(',')))
        break
maxx, minn = max(arr), min(arr)

minimum_cost = 100000000000000
for target in range(minn, maxx + 1):
    cost = 0
    for num in arr:
        cost += abs(num - target)

    minimum_cost = min(minimum_cost, cost)

print(minimum_cost)

