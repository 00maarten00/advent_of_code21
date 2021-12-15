#wget --load-cookies=cookies.txt https://adventofcode.com/2021/day/14/input
import parser as p
lst = p.singleparse("input14")
polymer = lst[0]

def most_frequent(List):
    return max(set(List), key = List.count)

def least_frequent(List):
    return min(set(List), key = List.count)

instructions = []
reslst = []
for i in lst[2:]:
    temp = i.split(" -> ")
    instructions.append((temp[0],temp[1]))
    reslst.append(temp[0])
res = {i : 0 for i in reslst}

    
def update(lst,dictionar):
    for i in range(len(lst)-1):
        dictionar[lst[i:i+2]] += 1
    return dictionar

res = update(polymer,res)

loopcount = 40

for nothing in range(loopcount):
    to_add = []
    to_remove = []
    for instruction in instructions:
        if res[instruction[0]] != 0:
            to_add.append((instruction[0][0]+instruction[1],res[instruction[0]]))
            to_add.append((instruction[1]+instruction[0][1],res[instruction[0]]))
            to_remove.append(instruction[0])
    for remove in to_remove:
        res[remove] = 0

    for add in to_add:
        res[add[0]] += add[1]
    
def calculate(dictionary):
    result = {}
    for lettercombo in dictionary:
        if lettercombo[0] in result:
            result[lettercombo[0]] += dictionary[lettercombo]
        else:
            result[lettercombo[0]] = dictionary[lettercombo]
        if lettercombo[1] in result:
            result[lettercombo[1]] += dictionary[lettercombo]
        else:
            result[lettercombo[1]] = dictionary[lettercombo]
    maximum = max(result, key=result.get)
    minimum = min(result, key=result.get)
    if maximum == polymer[0] or maximum == polymer[-1]:
        result[maximum] += 1
    if minimum == polymer[0] or minimum == polymer[-1]:
        result[minimum] += 1

    return (result[maximum]/2,result[minimum]/2)

answer = calculate(res)
print(answer[0]-answer[1])


    

         
