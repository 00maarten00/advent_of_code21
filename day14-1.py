#wget --load-cookies=cookies.txt https://adventofcode.com/2021/day/14/input
import parser as p
lst = p.singleparse("input14")
polymer = lst[0]

def most_frequent(List):
    return max(set(List), key = List.count)

def least_frequent(List):
    return min(set(List), key = List.count)

res = []
for i in lst[2:]:
    temp = i.split(" -> ")
    res.append((temp[0],temp[1]))

instructions = res

loopcount = 10

for nothing in range(loopcount):
    to_change = []
    for instruction in instructions:
        index = [i for i in range(len(polymer)) if polymer.startswith(instruction[0], i)]
        if  index != []:
            for i in index:
                to_change.append((i,instruction[1]))
    to_change.sort()
    counter = 1
    for change in to_change:
        polymer = polymer[:change[0]+counter] + change[1] + polymer[change[0]+counter:]
        counter += 1
    

print(polymer.count(most_frequent(polymer))-polymer.count(least_frequent(polymer)))           
