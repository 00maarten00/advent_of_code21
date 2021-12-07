#wget --load-cookies=cookies.txt https://adventofcode.com/2021/day/3/input
import parser as p
lst = p.singleparse("input3")
a=[]
b=[]
c=0
d=0

for j in range(len(lst[0])):
    for i in range(len(lst)):
        if lst[i][j] == '1':
            c +=1
        else:
            d +=1
    
    if c >= d:
        a.append("1")
        b.append("0")

    else:
        a.append("0")
        b.append("1")
    c=0
    d=0
print(int("".join(a),2)*int("".join(b),2))