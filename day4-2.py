#wget --load-cookies=cookies.txt https://adventofcode.com/2021/day/4/input
import parser as p
lst = p.autoparse("input4")

draw = list(map(int,"".join(lst[0]).split(",")))
del lst[0]
lst = [i for i in lst if i != []]

def getBoardSum(row,winning):
    start = row-(row%5)
    answer = [lst[start],lst[start+1],lst[start+2],lst[start+3],lst[start+4],winning]
    result = []
    for i in range(len(answer)-1):
        result = result + [int(j) for j in answer[i] if j != "checked"]
    return sum(result)*answer[-1]    

def removeBoard(row):
    start = row-(row%5)
    del lst[start:start+5]

def checkRowBingo(drawn,bingo):
    j=0
    while j < len(lst) and bingo == False:
        if all(i == "checked" for i in lst[j]):
            if len(lst)==5:
                answer = getBoardSum(j,drawn)
                print(answer)
                return True
            else:
                removeBoard(j)
                checkRowBingo(drawn,bingo)
                return
            
        j += 1
def checkColumnBingo(drawn,bingo):
    j=0
    toRemove = []
    while j < len(lst) and bingo == False:
        for k in range(5):
            if all(i == "checked" for i in [lst[j][k],lst[j+1][k],lst[j+2][k],lst[j+3][k],lst[j+4][k]]):
                if len(lst)<=5:
                    answer = getBoardSum(j,drawn)
                    print(answer)
                    return True
                    
                else:
                    removeBoard(j)
                    checkColumnBingo(drawn,bingo)
                    return

                
        j += 5
bingo = False
while bingo == False:
    for drawn in draw:

        for j in range(len(lst)):
            lst[j] = ["checked" if (i == "checked" or int(i) == drawn) else i for i in lst[j]]

        if checkRowBingo(drawn,bingo):
            bingo = True
        
        if checkColumnBingo(drawn,bingo):
            bingo = True

        if bingo:
            break
        


                
                    







