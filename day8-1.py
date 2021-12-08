#wget --load-cookies=cookies.txt https://adventofcode.com/2021/day/8/input
import parser as p
lst = p.autoparse("input")
lst2 = []
for i in lst:
    lst2 += i[11:]

counter = 0
for i in lst2:
    if len(i) == 2 or len(i) == 3 or len(i) == 4 or len(i) == 7:
        counter += 1
print(counter)