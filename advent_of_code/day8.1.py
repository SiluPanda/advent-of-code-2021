from sys import stdin

count = 0

for line in stdin:
    if line != '\n':
        values = line.split('|')[1].split(' ')

        for value in values:
            value = value.lstrip()
            value = value.rstrip()
            print(value, len(value))
            if len(value) in [2, 4, 3, 7]:
                count += 1

print(count)


