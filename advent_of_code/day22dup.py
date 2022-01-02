#!/usr/bin/env python3

import re
from dataclasses import dataclass, field

with open('input22.txt') as fh:
    data = fh.read()

@dataclass(unsafe_hash=True, repr=True)
class Cuboid:
    """A rectangular box"""
    x0: int
    x1: int
    y0: int
    y1: int
    z0: int
    z1: int
    on: bool = field(default=False, compare=False)
        
    @property
    def size(self):
        return (self.x1 - self.x0 + 1) * (self.y1 - self.y0 + 1) * (self.z1 - self.z0 + 1)

    @property
    def coords(self):
        return(self.x0, self.x1, self.y0, self.y1, self.z0, self.z1)
    
    def intersect(self, other):
        x10 = max(self.x0, other.x0)
        x11 = min(self.x1, other.x1)
        y10 = max(self.y0, other.y0)
        y11 = min(self.y1, other.y1)
        z10 = max(self.z0, other.z0)
        z11 = min(self.z1, other.z1)
        if x10 <= x11 and y10 <= y11 and z10 <= z11:
            return Cuboid(x10, x11, y10, y11, z10, z11, on=self.on)
    
    def subtract(self, other):
        """Return up to 6 rectangular boxes after removing the intersection with other"""
        subcbd = self.intersect(other)
        if subcbd is None:
            return [self]
        L = []
        (x00, x01, y00, y01, z00, z01) = self.coords
        (x10, x11, y10, y11, z10, z11) = subcbd.coords
        if x00 < x10:
            L.append(Cuboid(x00, x10-1, y00, y01, z00, z01, on=self.on))
        if x01 > x11:
            L.append(Cuboid(x11+1, x01, y00, y01, z00, z01, on=self.on))
        if y00 < y10:
            L.append(Cuboid(x10, x11, y00, y10-1, z00, z01, on=self.on))
        if y01 > y11:
            L.append(Cuboid(x10, x11, y11+1, y01, z00, z01, on=self.on))
        if z00 < z10:
            L.append(Cuboid(x10, x11, y10, y11, z00, z10-1, on=self.on))
        if z01 > z11:
            L.append(Cuboid(x10, x11, y10, y11, z11+1, z01, on=self.on))
        return L
    
    @classmethod
    def from_string(cls, s):
        """on x=-20..26,y=-36..17,z=-47..7"""
        onoff_str, coords = s.split()
        cbd = cls(*tuple(int(n) for n in re.findall(r'-?\d+', coords)))
        cbd.on = onoff_str == 'on'
        return cbd
    

def initialize_(data):
    S = set()
    central = Cuboid(-50, 50, -50, 50, -50, 50)
    for line in data.strip().split('\n'):
        cbd = Cuboid.from_string(line).intersect(central)
        if cbd is None:
            continue
        for other in list(S):
            S.remove(other)
            S.update(other.subtract(cbd))
        S.add(cbd)
    return sum(x.size for x in S if x.on)

part_1 = initialize_(data)
print('part_1 =', part_1)

## Part 2

def reboot(data):
    S = set()
    for i, line in enumerate(data.strip().split('\n')):
        cbd = Cuboid.from_string(line)
        for other in list(S):
            S.remove(other)
            S.update(other.subtract(cbd))
        S.add(cbd)
        print("=======")
        for x in S:
            if i < 5: 
                print(x)
    return sum(x.size for x in S if x.on)

part_2 = reboot(data)
print('part_2 =', part_2)