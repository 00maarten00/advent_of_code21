#wget --load-cookies=cookies.txt https://adventofcode.com/2021/day/9/input
import parser as p
from typing import List
lst = p.autoparse("input9")
counter = []

def get_basin(i,j,size):
    if j != len(lst[i][0])-1 and int(lst[i][0][j+1]) != 9 and int(lst[i][0][j]) < int(lst[i][0][j+1]):
        size.append((i,j+1))
        get_basin(i,j+1,size)
    if j != 0 and int(lst[i][0][j-1]) != 9 and int(lst[i][0][j]) < int(lst[i][0][j-1]):
        size.append((i,j-1))
        get_basin(i,j-1,size)
    if i != len(lst)-1 and int(lst[i+1][0][j]) != 9 and int(lst[i][0][j]) < int(lst[i+1][0][j]):
        size.append((i+1,j))
        get_basin(i+1,j,size)
    if i != 0 and int(lst[i-1][0][j]) != 9 and int(lst[i][0][j]) < int(lst[i-1][0][j]):
        size.append((i-1,j))
        get_basin(i-1,j,size)
    return len(list(dict.fromkeys(size))) + 1
   


for i in range(len(lst)):
    for j in range(len(lst[i][0])):

        if j != 0 and j != len(lst[i][0])-1 and i !=0 and i != len(lst)-1:
            if int(lst[i][0][j]) < int(lst[i][0][j-1]) and int(lst[i][0][j]) < int(lst[i][0][j+1]) and int(lst[i][0][j]) < int(lst[i-1][0][j]) and int(lst[i][0][j]) < int(lst[i+1][0][j]):
                counter.append(get_basin(i,j,[]))

        elif j != len(lst[i][0])-1 and i !=0 and i != len(lst)-1:
            if int(lst[i][0][j]) < int(lst[i][0][j+1]) and int(lst[i][0][j]) < int(lst[i-1][0][j]) and int(lst[i][0][j]) < int(lst[i+1][0][j]):
                counter.append(get_basin(i,j,[]))
        elif j != 0 and i !=0 and i != len(lst)-1:
            if int(lst[i][0][j]) < int(lst[i][0][j-1]) and int(lst[i][0][j]) < int(lst[i-1][0][j]) and int(lst[i][0][j]) < int(lst[i+1][0][j]):
                counter.append(get_basin(i,j,[]))
        elif j != 0 and j != len(lst[i][0])-1 and i != len(lst)-1:
            if int(lst[i][0][j]) < int(lst[i][0][j-1]) and int(lst[i][0][j]) < int(lst[i][0][j+1]) and int(lst[i][0][j]) < int(lst[i+1][0][j]):
                counter.append(get_basin(i,j,[]))
        elif j != 0 and j != len(lst[i][0])-1 and i !=0:
            if int(lst[i][0][j]) < int(lst[i][0][j-1]) and int(lst[i][0][j]) < int(lst[i][0][j+1]) and int(lst[i][0][j]) < int(lst[i-1][0][j]):
                counter.append(get_basin(i,j,[]))

        elif j==0 and i==0:
            if int(lst[i][0][j]) < int(lst[i][0][j+1]) and int(lst[i][0][j]) < int(lst[i+1][0][j]):
                counter.append(get_basin(i,j,[]))
        elif j==0 and i == len(lst)-1:
            if int(lst[i][0][j]) < int(lst[i][0][j+1]) and int(lst[i][0][j]) < int(lst[i-1][0][j]):
                counter.append(get_basin(i,j,[]))
        elif j==len(lst[i][0])-1 and i == 0:
            if int(lst[i][0][j]) < int(lst[i][0][j-1]) and int(lst[i][0][j]) < int(lst[i+1][0][j]):
                counter.append(get_basin(i,j,[]))
        elif j==len(lst[i][0])-1 and i == len(lst)-1:
            if int(lst[i][0][j]) < int(lst[i][0][j-1]) and int(lst[i][0][j]) < int(lst[i-1][0][j]):
                counter.append(get_basin(i,j,[]))
        else:
            print("error",i,j)
counter.sort()
print(counter[-1]*counter[-2]*counter[-3])