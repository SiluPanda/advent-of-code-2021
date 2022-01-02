from sys import stdin


mat = []
for line in stdin:
    if line != '\n':
        line = line.lstrip()
        line = line.rstrip()


        row = [int(c) for c in line]

        mat.append(row)


def step(mat):
    N, M = len(mat), len(mat[0])
    
    for i in range(N):
        for j in range(M):
            mat[i][j] += 1

    visited = [[False for j in range(M)] for i in range(N)]
    flashes = 0
    for i in range(N):
        for j in range(M):
            if mat[i][j] >= 10 and not visited[i][j]:
                dfs = [[i, j]]
                visited[i][j] = True

                
                while dfs:
                    x, y = dfs.pop()
                    flashes += 1
                    mat[x][y] = 0

                    for d in [[0, 1], [0, -1], [1, 0], [-1, 0], [1, -1], [1, 1], [-1, 1], [-1, -1]]:
                        p, q = x + d[0], y + d[1]

                        if 0 <= p < N and 0 <= q < M and not visited[p][q]:
                            mat[p][q] += 1
                            if mat[p][q] >= 10:
                                visited[p][q] = True
                                dfs.append([p, q])

    return flashes



count = 0
while True:
    curr_flash = step(mat)
    count += 1
    if curr_flash == len(mat) * len(mat[0]):
        print(count)
        break
    # print("============")
    # for x in mat:
    #     for y in x:
    #         print(y, end=' ')
    #     print()


                
