#wget --load-cookies=cookies.txt https://adventofcode.com/2021/day/3/input
import parser as p
lst = p.singleparse("input3")
a=0
b=0
c=0
d=0

for j in range(len(lst[0])):
    for i in range(len(lst)):
        if lst[i][j] == '1':
            c +=1
        else:
            d +=1
    
    if c >= d:
        i = 0       
        while len(lst)>1 and i < len(lst):
            if lst[i][j] == '0':
                del lst[i]
                i = 0
            else:
                i+=1

    else:
        i=0
        while len(lst)>1 and i < len(lst):
            if lst[i][j] == '1':
                del lst[i]
                i = 0
            else:
                i+=1
    c =0
    d = 0
a=lst[0]


lst = p.singleparse("input3")
c=0
d=0

for j in range(len(lst[0])):
    for i in range(len(lst)):
        if lst[i][j] == '1':
            c +=1
        else:
            d +=1
    
    if c >= d:
        i = 0       
        while len(lst)>1 and i < len(lst):
            if lst[i][j] == '1':
                del lst[i]
                i = 0
            else:
                i+=1

    else:
        i=0
        while len(lst)>1 and i < len(lst):
            if lst[i][j] == '0':
                del lst[i]
                i = 0
            else:
                i+=1
    c =0
    d = 0
b=lst[0]
print(int(a,2)*int(b,2))