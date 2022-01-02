from sys import stdin
from typing import DefaultDict


mat = []

inf = 100000000000
for line in stdin:
    if line != '\n':
        line = line.lstrip().rstrip()

        row = [int(s) for s in list(line)]
        mat.append(row)

N, M = len(mat), len(mat[0])

def get_min_node(distances, visited):
    min_node = None
    min_distance = inf

    for node in distances:
        if not visited[node] and distances[node] < min_distance:
            min_distance = distances[node]
            min_node = node

    return min_node

distances = {}
visited = {}
for i in range(N):
    for j in range(M):
        distances[(i, j)] = inf
        visited[(i, j)] = False


distances[(0, 0)] = mat[0][0]


for i in range(N * M):
    min_node = get_min_node(distances, visited)
    visited[min_node] = True

    for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        p, q = min_node[0] + d[0], min_node[1] + d[1]
        if 0 <= p < N and 0 <= q < M and distances[(p, q)] > distances[min_node] + mat[p][q]:
            distances[(p, q)] = distances[min_node] + mat[p][q]


# print(distances)
print(distances[(N - 1, M - 1)] - distances[(0, 0)])

