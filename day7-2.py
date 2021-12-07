#wget --load-cookies=cookies.txt https://adventofcode.com/2021/day/7/input
import parser as p
lst = p.commaparse("input7")
lst = list(map(int,lst))

minimum = 0
cost = [0]*(max(lst)+1)

for i in range(0,max(lst)+1):
    if i == 0:
        cost[i] = 0
    else:
        cost[i] = i + cost[i-1]

for i in range(min(lst),max(lst)+1):
    total = 0
    for j in lst:
        total += cost[abs(i-j)]
    if minimum == 0 or total < minimum:
        minimum = total
print(minimum)