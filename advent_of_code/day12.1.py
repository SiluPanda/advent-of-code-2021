from sys import stdin
from collections import defaultdict


graph = defaultdict(list)

for line in stdin:
    if line != '\n':
        line = line.lstrip().rstrip()
        src, dest = line.split('-')
        graph[src].append(dest)
        graph[dest].append(src)


def is_big_cave(cave):
    return not cave.lower() == cave


def is_valid(path, neigh):
    seen = False
    count = 0
    curr_path = path.copy()
    curr_path[neigh] += 1
    if curr_path[neigh] > 2:
        return False
    for node in curr_path:
        if is_big_cave(node):
            continue
        else:
            count += curr_path[node] > 1

    
    return count <= 1

def count_paths(graph, curr_path, path, curr_node, count):
    if curr_node == 'end':
        count[0] += 1
        
    else:
        for neigh in graph[curr_node]:
            if neigh == 'start':
                continue

            if is_big_cave(neigh) or is_valid(curr_path, neigh):
                new_path = curr_path.copy()
                new_path[neigh] += 1
                count_paths(graph, new_path, path, neigh, count)
                


count = [0]
path = ['start']
curr_path = defaultdict(int)
count_paths(graph, curr_path, path, 'start', count)

print(count[0])
