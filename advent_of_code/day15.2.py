from sys import stdin
from typing import DefaultDict
from heapq import *


mat = []

inf = 100000000000
for line in stdin:
    if line != '\n':
        line = line.lstrip().rstrip()

        row = [int(s) for s in list(line)]
        mat.append(row)



def get_min_node(distances, visited):
    min_node = None
    min_distance = inf

    for node in distances:
        if not visited[node] and distances[node] < min_distance:
            min_distance = distances[node]
            min_node = node

    return min_node

def generate_new_mat(mat):

    N, M = len(mat), len(mat[0])
    ret = [[0 for j in range(M * 5)] for i in range(N * 5)]
    for i in range(N * 5):
        for j in range(M * 5):
            # ret[i][j] = (mat[i % N][j % M] + (i // N) + (j // M))
            # if ret[i][j] >= 10:
            #     ret[i][j] = 1

            if j < M:
                if i < N:
                    ret[i][j] = mat[i][j]
                else:
                    ret[i][j] = ret[i-N][j] + 1
            else:
                ret[i][j] = ret[i][j-M] + 1

            if ret[i][j] > 9:
                ret[i][j] = 1

    for x in ret:
        for y in x:
            print(y, end='')
        print()
    return ret

    

mat = generate_new_mat(mat)
N, M = len(mat), len(mat[0])
distances = {}

dheap = []
for i in range(N):
    for j in range(M):
        distances[(i, j)] = inf
        


distances[(0, 0)] = mat[0][0]
heappush(dheap, (mat[0][0], 0, 0))


while dheap:
    top = heappop(dheap)
    distt = top[0]
    min_node = tuple(top[1:])
    if distt != distances[min_node]:
        continue
    
    

    for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        p, q = min_node[0] + d[0], min_node[1] + d[1]
        if 0 <= p < N and 0 <= q < M and distances[(p, q)] > distances[min_node] + mat[p][q]:
            distances[(p, q)] = distances[min_node] + mat[p][q]
            heappush(dheap, (distances[(p, q)], p, q))


# print(distances)
print(distances[(N - 1, M - 1)] - distances[(0, 0)])

