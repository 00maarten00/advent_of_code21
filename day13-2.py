#wget --load-cookies=cookies.txt https://adventofcode.com/2021/day/13/input
import parser as p
lst = p.singleparse("input")
dots = lst[:1022]
instr = lst[1023:]

res = []
for i in dots:
    temp = i.split(",")
    res.append((int(temp[0]),int(temp[1])))

dots = res

res = []
for i in instr:
    templst = i.split(" ")
    temp = templst[2]
    instrlst = temp.split("=")
    res.append((instrlst[0],int(instrlst[1])))

instr = res

for i in instr:
    for j in range(len(dots)):
        if i[0] == "x":
            if dots[j][0] > i[1]:
                dots[j] = (i[1] - (dots[j][0] - i[1]),dots[j][1])
        if i[0] == "y":
            if dots[j][1] > i[1]:
                dots[j] = (dots[j][0],i[1] - (dots[j][1] - i[1]))

def draw(dots):
    xlst = [i[0] for i in dots]
    ylst = [i[1] for i in dots]
    xmax = max(xlst)
    ymax = max(ylst)
    for y in range(ymax+1):
        to_draw = ""
        for x in range(xmax+1):
            if (x,y) in dots:
                to_draw += "#"
            else:
                to_draw += " "
        print(to_draw)
        
dots = list(dict.fromkeys(dots))
draw(dots)
