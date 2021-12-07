#wget --load-cookies=cookies.txt https://adventofcode.com/2021/day/4/input
import parser as p
lst = p.autoparse("input4")

draw = list(map(int,"".join(lst[0]).split(",")))
del lst[0]
lst = [i for i in lst if i != []]

def getBoardSum(row,winning):
    start = row-(row%5)
    return [lst[start],lst[start+1],lst[start+2],lst[start+3],lst[start+4],winning]


bingo = False
answer = 0
while bingo == False:
    for drawn in draw:

        for j in range(len(lst)):
            lst[j] = ["checked" if (i == "checked" or int(i) == drawn) else i for i in lst[j]]

        j=0
        while j < len(lst) and bingo == False:
            if all(i == "checked" for i in lst[j]):
                answer = getBoardSum(j,drawn)
                bingo = True
                break
            j += 1
        
        j=0
        while j < len(lst) and bingo == False:
            for k in range(5):
                if all(i == "checked" for i in [lst[j][k],lst[j+1][k],lst[j+2][k],lst[j+3][k],lst[j+4][k]]):
                    answer = getBoardSum(j,drawn)
                    bingo = True
                    break
            j += 5
        if bingo:
            break
        
result = []
for i in range(len(answer)-1):
    result = result + [int(j) for j in answer[i] if j != "checked"]
print(sum(result)*answer[-1])                
                    







