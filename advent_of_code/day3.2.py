from sys import stdin


F = set()
for line in stdin:
    if line != '\n':
        if line[-1] == '\n':
            line = line[:-1]

        F.add(line)


G = F.copy()

pos = 0
while len(F) > 1:
    one = 0
    zero = 0
    for num in F:
        if num[pos] == '0':
            zero += 1
        else:
            one += 1

    to_remove = []
    if one >= zero:
        for num in F:
            if num[pos] != '1':
                to_remove.append(num)

    else:
        for num in F:
            if num[pos] != '0':
                to_remove.append(num)


    for num in to_remove:
        F.remove(num)
    
    pos += 1


pos = 0

while len(G) > 1:
    one = 0
    zero = 0
    for num in G:
        if num[pos] == '1':
            one += 1
        else:
            zero += 1
    
    to_remove = []
    if zero <= one:
        for num in G:
            if num[pos] != '0':
                to_remove.append(num)

    else:
        for num in G:
            if num[pos] != '1':
                to_remove.append(num)


    for num in to_remove:
        G.remove(num)


    pos += 1


x, y = 0, 0
for num in F:
    x = num

for num in G:
    y = num

print(int(x, 2) * int(y, 2))

        