from sys import stdin

x, y, aim = 0, 0, 0

for line in stdin:
    if line != '\n':
        command, value = line.split()
        value = int(value)

        print(command, value)

        if command == 'forward':
            x += value
            y += aim * value

        elif command == 'down':
            aim += value
        
        else:
            aim -= value

        print(x, y, aim)
print(x * y)