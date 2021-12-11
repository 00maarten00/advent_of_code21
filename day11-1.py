#wget --load-cookies=cookies.txt https://adventofcode.com/2021/day/11/input
import parser as p
lst = p.singleparse("input")

for i in range(len(lst)):
    lst[i] = list(map(int,lst[i]))

global flashed

flashed = []

def do_light(row,column,incr):
    lst[row][column] += incr
    if lst[row][column] > 9:
        flashed.append((row,column))
        counter = 1
        lst[row][column] = 0
        if row != 0:
            counter += do_light(row-1,column,1)
        if row != len(lst)-1:
            counter += do_light(row+1,column,1)
        if column != 0:
            counter += do_light(row,column-1,1)
        if column != len(lst[row])-1:
            counter += do_light(row,column+1,1)
        if column != 0 and row != 0:
            counter += do_light(row-1,column-1,1)
        if column != len(lst[row])-1 and row != 0:
            counter += do_light(row-1,column+1,1)
        if row != len(lst)-1 and column != 0:
            counter += do_light(row+1,column-1,1)
        if row != len(lst)-1 and column != len(lst[row])-1:
            counter += do_light(row+1,column+1,1)
        lst[row][column] = 0
        return counter
    else:
        return 0

def print_board(lst):
    for i in lst:
        print(i)
    print()

def set_to_zero(to_zero,lst):
    for i in to_zero:
        lst[i[0]][i[1]] = 0
    return lst


def do_round(lst, rounds):
    c = 0
    for i in range(rounds):
        global flashed
        flashed = []
        for j in range(len(lst)):
            for z in range(len(lst[j])):
                lst[j][z] += 1
                if lst[j][z] > 9:
                    c += do_light(j,z,0)
        lst = set_to_zero(flashed,lst)
    return c
                
print(do_round(lst,100))