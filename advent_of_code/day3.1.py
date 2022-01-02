from sys import stdin


frequency = None
for line in stdin:
    
    if line != '\n':
        

        line = line[:-1]
        if not frequency:
            frequency = [[0, 0] for i in range(len(line))]
        
        for i in range(len(line)):
            if line[i] == '1':
                frequency[i][1] += 1
            else:
                frequency[i][0] += 1


print(len(frequency))

x, y = '', ''
for i in range(len(frequency)):
    if frequency[i][0] > frequency[i][1]:
        x += '0'
        y += '1'
    else:
        x += '1'
        y += '0'

print(x, y)

print(int(x, 2) * int(y, 2))