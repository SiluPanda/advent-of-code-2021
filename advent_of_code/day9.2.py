from sys import stdin


def get_basin_size(matrix, x, y):
    dfs = [[x, y]]
    N, M = len(matrix), len(matrix[0])
    count = 0
    visited = [[False for j in range(M)] for i in range(N)]
    while dfs:
        cx, cy = dfs.pop()
        count += 1

        for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx, ny = cx + d[0], cy + d[1]

            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] != 9 and matrix[nx][ny] > matrix[cx][cy] and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs.append([nx, ny])

    return count     


matrix = []
for line in stdin:
    if line != '\n':
        line = line.strip()
        line = line.lstrip()

        matrix.append([int(x) for x in list(line)])


basins = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        good = True
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = i + d[0], j + d[1]

            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] <= matrix[i][j]:
                good = False
                break

        if good:
            basins.append(get_basin_size(matrix, i, j))

basins.sort(reverse=True)

ans = 1
for i in range(3):
    ans *= basins[i]

print(ans)