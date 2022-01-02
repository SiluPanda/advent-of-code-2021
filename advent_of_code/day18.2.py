from sys import stdin
import math
from typing import *




def tokenize(s: str) -> List[Union[str, int]]:
    ret = []
    i = 0
    
    while i < len(s):
        if s[i].isdigit():
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            ret.append(int(s[i:j]))
            i = j
        else:
            ret.append(s[i])
            i += 1

    return ret


def explode(s: List[Union[int, str]], i: int) -> List[Union[int, str]]:
    left, right = s[i+1], s[i+3]
    j = i
    while j >= 0 and isinstance(s[j], str):
        j -= 1
    if j >= 0:
        s[j] += left

    j = i + 4
    while j < len(s) and isinstance(s[j], str):
        j += 1
    if j < len(s):
        s[j] += right

    s[i:i+5] = [0]

    return s

def split(s: List[Union[int, str]], i: int) -> List[Union[int, str]]:
    s[i:i+1] = ['[', math.floor(s[i] / 2), ',', math.ceil(s[i]/ 2), ']']
    return s


def join_tokens(s: List[Union[int, str]]) -> str:
    return ''.join([str(x) for x in s])


def reduce(s: str) -> str:
    s = tokenize(s)
    open_parenthesis = 0
    for i in range(len(s)):
        if isinstance(s[i], str):
            if s[i] == '[':
                open_parenthesis += 1
            elif s[i] == ']':
                open_parenthesis -= 1

            if open_parenthesis > 4:
                s = explode(s, i)
                s = reduce(join_tokens(s))
                break

    for i in range(len(s)):
        if isinstance(s[i], int) and s[i] >= 10:
            s = split(s, i)
            s = reduce(join_tokens(s))
            break

    return join_tokens(s)

def compute_magnitude(number: Union[int, List[object]]) -> int:
    if isinstance(number, int):
        return number
    
    else:
        return 3 * compute_magnitude(number[0]) + 2 * compute_magnitude(number[1])

def add(a: str, b: str) -> str:
    return reduce(f'[{a},{b}]')


expressions = []
for line in stdin:
    if line != '\n':
        line = line.lstrip().rstrip()

        expressions.append(line)


maximum = 0
for i in range(len(expressions)):
    for j in range(len(expressions)):
        if i != j:
            s = add(expressions[i], expressions[j])
            number = eval(s)
            maximum = max(maximum, compute_magnitude(number))


print(maximum)




    
    




                

        
