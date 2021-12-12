#wget --load-cookies=cookies.txt https://adventofcode.com/2021/day/12/input
import parser as p
from typing import List
lst = p.singleparse("input12")

for i in range(len(lst)):
    splitted = lst[i].split("-")
    lst[i] = (splitted[0],splitted[1])

def get_connected_caves(cave):
    res = []
    for i in lst:
        if i[0] == cave and i[1] != "start":
            res.append(i[1])
        if i[1] == cave and i[0] != "start":
            res.append(i[0])
    return res

def is_big_cave(cave):
    return cave.isupper()


def getroutes(startroute):
    routes = []
    for i in get_connected_caves(startroute[-1]):
        routes.append(startroute+[i])
    return routes


old = (getroutes(["start"]))
counter = 0
while True:
    new = []
    for i in old:
        if i[-1] != "end":
            if is_big_cave(i[-1]):
                new = new + getroutes(i)
            else:
                if i.index(i[-1]) == len(i)-1:
                    new = new + getroutes(i)
                else:
                    small_caves = [j for j in i[:-1] if not is_big_cave(j)]
                    small_caves2 = set(small_caves)
                    if len(small_caves) == len(small_caves2):
                        new = new + getroutes(i)

        else:
            counter += 1
    if all(i[-1]=="end" for i in new):
        break

    old = new

print(counter)

    
    
            

