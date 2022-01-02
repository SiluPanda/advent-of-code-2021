from sys import stdin



grid = [[0 for j in range(1000)] for i in range(1000)]

for line in stdin:
    if line != '\n':
        src, dest = line.split('->')

        x, y = map(int, src.split(','))
        p, q = map(int, dest.split(','))

        if max(x, y, p, q) >= 1000:
            raise Exception('no')

        # if horizontal or vertical or diagonal
        if x == p:
            for j in range(min(y, q), max(y, q) + 1):
                grid[x][j] += 1
        
        elif y == q:
            for i in range(min(x, p), max(x, p) + 1):
                grid[i][y] += 1

        elif abs(x - p) == abs(y - q):
            if x > p:
                x, p = p, x
                y, q = q, y

            if y < q:
                a, b = x, y
                while True:
                    grid[a][b] += 1
                    if a == p and b == q:
                        break
                    a += 1
                    b += 1
            else:
                a, b = x, y
                while True:
                    grid[a][b] += 1
                    if a == p and b == q:
                        break
                    a += 1
                    b -= 1


ret = 0
for i in range(1000):
    for j in range(1000):
        ret += grid[i][j] > 1

print(ret)
        