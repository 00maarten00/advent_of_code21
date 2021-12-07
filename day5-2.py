#wget --load-cookies=cookies.txt https://adventofcode.com/2021/day/5/input
import parser as p
from collections import Counter
lst = p.autoparse("input5")

def createLine(point1,point2):
    point1 = point1.split(",")
    point2 = point2.split(",")
    x1 = int(point1[0])
    y1 = int(point1[1])
    x2 = int(point2[0])
    y2 = int(point2[1])
    result = []
    if x1 == x2:
        if y1 < y2:
            for i in range(y2+1-y1):
                result.append((x1,y1+i))
        else:
            for i in range(y1+1-y2):
                result.append((x1,y2+i))
    elif y1 == y2:
        if x1 < x2:
            for i in range(x2+1-x1):
                result.append((x1+i,y1))
        else:
            for i in range(x1+1-x2):
                result.append((x2+i,y1))
    else:
        if x1<x2:
            if y1<y2:
                for i in range(x2+1-x1):
                    result.append((x1+i,y1+i))
            else:
                for i in range(x2+1-x1):
                    result.append((x1+i,y1-i))
        else:
            if y1<y2:
                for i in range(x1+1-x2):
                    result.append((x1-i,y1+i))
            else:
                for i in range(x1+1-x2):
                    result.append((x2+i,y2+i))       
    return result


end_result = []
for i in lst:
    end_result = end_result + createLine(i[0],i[2])

count=Counter(end_result)
values = count.values()
countlist = [i for i in values if i > 1]
print(len(countlist))