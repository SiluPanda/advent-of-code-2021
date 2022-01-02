from sys import stdin
from collections import Counter, defaultdict


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

'''
ABCD -> ANBCXD


'''

curr_pairs = defaultdict(int)
for i in range(1, len(curr)):
    curr_pairs[curr[i-1:i+1]] += 1

counts = Counter(list(curr))
print(curr_pairs, rules)
for i in range(40):
    new_pairs = curr_pairs.copy()
    for rule in rules:
        if rule in curr_pairs:
            
            howmany = curr_pairs[rule]
            first_pair = rule[0] + rules[rule]
            second_pair = rules[rule] + rule[1]

            new_char = rules[rule]

            counts[new_char] += howmany
            new_pairs[rule] -= howmany
            new_pairs[first_pair] += howmany
            new_pairs[second_pair] += howmany
    curr_pairs = new_pairs.copy()
    # print(curr_pairs)



print(max(counts.values()) - min(counts.values()))

