from __future__ import annotations
from collections import *
from typing import *
import sys
import functools
import math


sys.setrecursionlimit(10 ** 7)


instructions = []
for line in open('input24.txt', 'r'):
    if line != '\n':
        line = line.lstrip().rstrip()

        instructions.append(line.split(' '))

@functools.lru_cache(maxsize=None)
def evaluate(inst_idx, w, x, y, z):

    if z > 10 ** 7:
        return False, ''
    
    if inst_idx == len(instructions):
        return (z == 0, '')

    

    values = {
        'x': x, 'y': y, 'z': z, 'w': w
    }
    if instructions[inst_idx][0] == 'inp':
        
        found = False
        for i in range(1, 10, 1):
            values[instructions[inst_idx][1]] = i
            ans = evaluate(inst_idx + 1, values['w'], values['x'], values['y'], values['z'])
            if ans[0]:
                found = True
                return True, str(i) + ans[1]

        if not found:
            return False, ''

    
    else:
        action = instructions[inst_idx][0]
        a, b = instructions[inst_idx][1:]
        
        if action == 'add':
            
            values[a] += get_or_int(values, b)
        elif action == 'mul':
            values[a] *= get_or_int(values, b)
        elif action == 'mod':
            if values[a] < 0 or get_or_int(values, b) <= 0:
                return False, ''
            values[a] = values[a] % get_or_int(values, b)
        elif action == 'eql':
            values[a] = 1 if values[a] == get_or_int(values, b) else 0 
        elif action == 'div':
            if get_or_int(values, b) == 0:
                return False, ''
            d = values[a] / get_or_int(values, b)

            values[a] = -math.floor(abs(d)) if d < 0 else math.floor(d)

        ans = evaluate(inst_idx + 1, values['w'], values['x'], values['y'], values['z'])
        if ans[0]:
            return True, ans[1]
        else:
            return False, ''
        


def get_or_int(map, key):
    if key in map:
        return map[key]
    else:
        return int(key)

        

memo = {}
print(evaluate(0, 0, 0, 0, 0))