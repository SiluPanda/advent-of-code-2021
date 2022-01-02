def can_reach(x, y, x1, x2, y1, y2):
    posx, posy = 0, 0
    my = 0
    while True:
        posx += x
        posy += y
        my = max(my, posy)

        if x1 <= posx <= x2 and y1 <= posy < y2:
            return True, my
        if x < 0:
            x += 1
        elif x > 0:
            x -= 1
        y -= 1

        if x == 0 and y < min(y1, y2):
            return False, None


    

x1, x2, y1, y2 = map(int, input().split())

my = 0
for x in range(-300, 300):
    for y in range(-300, 300):
        can, max_pos = can_reach(x, y, x1, x2, y1, y2)
        if can:
            # print(x, y)
            my = max(my, max_pos)

print(my)




