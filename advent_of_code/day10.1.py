from sys import stdin

points = {

    
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,

}

F = {
    ')': '(',
    '}': '{',
    ']': '[',
    '>': '<'
}

summ = 0
for line in stdin:
    if line != '\n':
        line = line.rstrip()
        line = line.lstrip()

        T = []
        for c in line:
            if c in ['(', '[', '{', '<']:
                T.append(c)
            else:
                if not T or T[-1] != F[c]:
                    summ += points[c]
                    break
                else:
                    T.pop()


print(summ)
                