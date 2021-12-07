#wget --load-cookies=cookies.txt https://adventofcode.com/2021/day/6/input
import parser as p
lst = p.commaparse("input6")
lst = list(map(int,lst))

def doDay(lst):
    result = []
    for i in lst:
        if i == 0:
            result += [6,8]
        else:
            result.append(i-1)
    return result

for i in range(1,81):
    lst = doDay(lst)

print(len(lst))