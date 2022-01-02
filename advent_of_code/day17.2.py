from typing import *

def can_reach(x: int, y: int, valid_destinations: Set[int], miny: int) -> bool:
    posx, posy = 0, 0
    
    while True:
        if x == 0:
            if y < 0 and posy < miny:
                return False

        posx += x
        posy += y

        if (posx, posy) in valid_destinations:
            return True
        
        y -= 1
        if x > 0:
            x -= 1
        elif x < 0:
            x += 1

    
        
        




x1, x2, y1, y2 = map(int, input().split())


valid_destinations = set()
for i in range(x1, x2 + 1):
    for j in range(y1, y2 + 1):
        valid_destinations.add((i, j))

unique_paths = 0
for x in range(0, 300):
    for y in range(-300, 500):
        can = can_reach(x, y, valid_destinations, min(y1, y2))
        if can:
            # print(x, y)
            unique_paths += 1

print(unique_paths)





