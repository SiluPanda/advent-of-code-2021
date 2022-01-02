from sys import stdin
from typing import MutableSet

def pprint(mat):
    for x in mat:
        for y in x:
            print(y, end=' ')
        print()

seen = False
numbers = []
boards = []
curr = []
for line in stdin:
    if not seen:
        numbers = list(map(int, line.split(',')))

        seen = True

    elif line == '\n':
        if curr:
            boards.append(curr)
        curr = []
    else:
        curr.append(list(map(int, line.split())))


if curr:
    boards.append(curr)


markings = [[[0 for j in range(5)] for i in range(5)] for k in range(len(boards))]

marked = set(list(range(len(boards))))
ended = False
for num in numbers:
    for k in range(len(boards)):
        for i in range(5):
            for j in range(5):
                if boards[k][i][j] == num:
                    markings[k][i][j] = 1


        # check if won
        win = False
        for row in markings[k]:
            if sum(row) == 5:
                win = True
                break
        
        for j in range(5):
            if sum([markings[k][i][j] for i in range(5)]) == 5:
                win = True
                break

        if win:
           
            # if last return ans
            if k in marked and len(marked) == 1:
                # compute
                summ = 0
                for i in range(5):
                    for j in range(5):
                        if not markings[k][i][j]:
                            summ += boards[k][i][j]

                
                print(summ * num)
                ended = True
                break

            else:
                if k  in marked:
                    marked.remove(k)

        


    if ended:
        break
    