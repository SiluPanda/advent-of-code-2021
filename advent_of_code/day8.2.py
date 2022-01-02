from sys import stdin

def decode_mapping(mapping):

    original = {
        'abcefg': 0,
        'cf': 1,
        'acdeg': 2,
        'acdfg': 3,
        'bcdf': 4,
        'abdfg': 5,
        'abdefg': 6,
        'acf': 7,
        'abcdefg': 8,
        'abcdfg': 9
    }
    char = {}
    F = {}
    for map in mapping:
        for c in map:
            F[c] = F.get(c, 0) + 1


    mapping.sort(key=lambda x: len(x))

    for map in mapping:
        if len(map) == 2:
            if F[map[0]] == 8:
                char[map[0]] = 'c'
                char[map[1]] = 'f'
            else:
                char[map[0]] = 'f'
                char[map[1]] = 'c'

        if len(map) == 3:
            for c in map:
                if c not in char:
                    char[c] = 'a'

        if len(map) == 4:
            for c in map:
                if F[c] == 7:
                    char[c] = 'd'  

    
    for c in F:
        if c not in char:
            if F[c] == 6:
                char[c] = 'b'
            if F[c] == 4:
                char[c] = 'e'
            if F[c] == 7:
                char[c] ='g' 

    reverse = {}
    for k, v in char.items():
        reverse[v] = k
    
    decoded = {}
    for k, v in original.items():
        new_key = ''
        for c in k:
            new_key += reverse[c]
        
        decoded[''.join(sorted(new_key))] = v

    return decoded

    
        




summ = 0
for line in stdin:
    if line != '\n':
        mappings, values = line.split('|')[0].split(' '), line.split('|')[1].split(' ')
        decoded = decode_mapping(mappings)
        num = ''
        for value in values:
            if len(value) == 0:
                continue
            value = value.lstrip()
            value = value.rstrip()
            num += str(decoded[''.join(sorted(value))])
        
        summ += int(num)

            

print(summ)