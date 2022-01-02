from sys import stdin

x, y = 0, 0

for line in stdin:
    if line != '\n':
        command, value = line.split()
        value = int(value)

        print(command, value)
        if command == 'forward':
            x += value
        elif command == 'down':
            y += value
        else:
            y -= value

print(x * y)