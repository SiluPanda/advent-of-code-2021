from __future__ import annotations, print_function
from typing import *
from collections import *
from dataclasses import dataclass



class Cuboid:
    def __init__(self, xmin: int, xmax: int, ymin: int, ymax: int, zmin: int, zmax: int, state: int) -> None:
        self.xmin = xmin
        self.xmax = xmax
        
        self.ymin = ymin
        self.ymax = ymax

        self.zmin = zmin
        self.zmax = zmax

        self.state = state

    
    def get_volume(self) -> int:
        return (self.xmax - self.xmin + 1) * (self.ymax - self.ymin + 1) * (self.zmax - self.zmin + 1)

    def get_intersection(self, other: Cuboid) -> Tuple[Union[bool, Optional[Cuboid]]]:
        x0 = max(self.xmin, other.xmin)
        x1 = min(self.xmax, other.xmax)

        y0 = max(self.ymin, other.ymin)
        y1 = min(self.ymax, other.ymax)

        z0 = max(self.zmin, other.zmin)
        z1 = min(self.zmax, other.zmax)

        if (x0 <= x1) and (y0 <= y1) and (z0 <= z1):
            return True, Cuboid(x0, x1, y0, y1, z0, z1, self.state)
        else:
            return False, None

    def get_substraction(self, ot: Cuboid) -> List[Cuboid]:
        has_intersection, other = self.get_intersection(ot)
        if not has_intersection:
            return [self]

        else:
            cubiobs = []
            if self.xmin < other.xmin:
                cubiobs.append(Cuboid(self.xmin, other.xmin - 1, self.ymin, self.ymax, self.zmin, self.zmax, self.state))
            if self.xmax > other.xmax:
                cubiobs.append(Cuboid(other.xmax + 1, self.xmax, self.ymin, self.ymax, self.zmin, self.zmax, self.state))
            if self.ymin < other.ymin:
                cubiobs.append(Cuboid(other.xmin, other.xmax, self.ymin, other.ymin - 1, self.zmin, self.zmax, self.state))
            if self.ymax > other.ymax:
                cubiobs.append(Cuboid(other.xmin, other.xmax, other.ymax + 1, self.ymax, self.zmin, self.zmax, self.state))
            if self.zmin < other.zmin:
                cubiobs.append(Cuboid(other.xmin, other.xmax, other.ymin, other.ymax, self.zmin, other.zmin - 1, self.state))
            if self.zmax > other.zmax:
                cubiobs.append(Cuboid(other.xmin, other.xmax, other.ymin, other.ymax, other.zmax + 1, self.zmax, self.state))

            return cubiobs

    def __str__(self) -> str:
        return f'{self.xmin}, {self.xmax}, {self.ymin}, {self.ymax}, {self.zmin}, {self.zmax}, {self.state}'



if __name__ == '__main__':   
    actions = []
    for line in open('input22.txt', 'r'):
        if line != '\n':
            line = line.rstrip().lstrip()
            action, coords = line.split(' ')
            xc, yc, zc = coords.split(',')
            
            xrange = list(map(int, xc.split('=')[1].split('..')))
            yrange = list(map(int, yc.split('=')[1].split('..')))
            zrange = list(map(int, zc.split('=')[1].split('..')))

            actions.append([1 if action == 'on' else 0, xrange, yrange, zrange])

    

    T = set()
    for i, action in enumerate(actions):
        cuboid = Cuboid(action[1][0], action[1][1], action[2][0], action[2][1], action[3][0], action[3][1], action[0])
        
        for existing in list(T):
            T.remove(existing)
            T.update(existing.get_substraction(cuboid))

        T.add(cuboid)
        
        if i < 5:
            print("=======")
            for t in T:
                print(t)


    total_volume = 0
    
    print(sum(x.get_volume() for x in T if x.state == 1))