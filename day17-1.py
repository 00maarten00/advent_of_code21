#wget --load-cookies=cookies.txt https://adventofcode.com/2021/day/17/input
import parser as p
lst = p.autoparse("input17")
xlower = 265
xupper = 287
ylower = -103
yupper = -58

def calculate(xvel,yvel):
    x = 0
    y = 0
    while x < xupper and y > ylower and not (xvel == 0 and (x < xlower or x > xupper)):
        if (xlower < x < xupper and ylower < y < yupper):
            return True
        x += xvel
        if xvel > 0 :
            xvel -= 1
        elif xvel < 0:
            xvel += 1
        y += yvel
        yvel -= 1
    return False

def get_max(xvel,yvel):
    x = 0
    y = 0
    while True:
        x += xvel
        if xvel > 0 :
            xvel -= 1
        elif xvel < 0:
            xvel += 1
        y += yvel
        if yvel == 0:
            return y
        yvel -= 1

print(get_max(23,102))

y = 0
while True:
    for x in range(xupper+1):
        if calculate(x,y):
            print(x,y+1)
            break
    y += 1

