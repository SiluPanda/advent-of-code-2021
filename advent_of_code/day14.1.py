from sys import stdin
from collections import Counter


rules = {}
curr = ""
for line in stdin:
    if line != '\n':
        line = line.lstrip().rstrip()
        if '-' in line:
            pat, c = line.split('->')
            pat = pat.lstrip().rstrip()
            c = c.lstrip().rstrip()
            rules[pat] = c
        else:
            curr = line



for i in range(40):
    print(i)
    new_line = curr[0]
    for j in range(1, len(curr)):
        # print(curr[j-1:j+1])
        if curr[j-1:j+1] in rules:
            # print("coming here")
            new_line += rules[curr[j-1:j+1]]
        new_line += curr[j]

    curr = new_line


F = Counter(list(curr))

print(max(F.values()) - min(F.values()))

