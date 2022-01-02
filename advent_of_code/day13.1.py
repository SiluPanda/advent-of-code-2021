from sys import stdin

coordinates = []
actions = []

for line in stdin:
    if line != '\n':
        line = line.rstrip().lstrip()
        tokens = line.split(',')
        if len(tokens) == 2:
            print(tokens)
            coordinates.append([int(tokens[0]), int(tokens[1])])
        else:
            tokens = line.split(' ')
            direction, value = tokens[2].split('=')
            value = int(value)
            actions.append([direction, value])


marked = set()
for c in coordinates:
    marked.add((c[0], c[1]))

for ac in actions:
    value = ac[1]
    to_delete = []
    to_add = []
    if ac[0] == 'x':
        for m in marked:
            if m[0] < value:
                to_delete.append(m)
                to_add.append((value - (m[0] - value), m[1]))
    else:
        for m in marked:
            if m[1] > value:
                to_delete.append(m)
                to_add.append((m[0], (value - (m[1] - value))))

    for m in to_delete:
        marked.remove(m)
    for m in to_add:
        marked.add(m)

    
    

maximum = 0
for m in marked:
    maximum = max(maximum, max(m))

p = [['.' for j in range(maximum + 1)] for i in range(maximum + 1)]
for m in marked:
    p[m[0]][m[1]] = '#'

for x in p:
    for y in x:
        print(y, end='')
    print()
