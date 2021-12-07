#wget --load-cookies=cookies.txt https://adventofcode.com/2021/day/7/input
import parser as p
lst = p.commaparse("input7")
lst = list(map(int,lst))
est = (sum(lst)//len(lst))
minimum = 0

for i in range(min(lst),max(lst)+1):
    total = 0
    for j in lst:
        total += abs(i-j)
    if minimum == 0 or total < minimum:
        minimum = total
print(minimum)