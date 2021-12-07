#wget --load-cookies=cookies.txt https://adventofcode.com/2021/day/6/input
import parser as p
lst = p.commaparse("input6")
lst = list(map(int,lst))
lst2 = [0]*9
for i in lst:
    lst2[i] += 1
    

def doDay(lst):
    result = [0]*9
    i = 0
    while i < 9:
        if i == 0:
            result[6] += lst[0]
            result[8] += lst[0]
        else:
            result[i-1] += lst[i]
        i +=1
    return result


for i in range(1,257):
    lst2 = doDay(lst2)

print(sum(lst2))
