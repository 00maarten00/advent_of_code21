#wget --load-cookies=cookies.txt https://adventofcode.com/2021/day/9/input
import parser as p
lst = p.autoparse("input9")
counter = 0

for i in range(len(lst)):
    for j in range(len(lst[i][0])):

        if j != 0 and j != len(lst[i][0])-1 and i !=0 and i != len(lst)-1:
            if int(lst[i][0][j]) < int(lst[i][0][j-1]) and int(lst[i][0][j]) < int(lst[i][0][j+1]) and int(lst[i][0][j]) < int(lst[i-1][0][j]) and int(lst[i][0][j]) < int(lst[i+1][0][j]):
                counter += int(lst[i][0][j]) + 1

        elif j != len(lst[i][0])-1 and i !=0 and i != len(lst)-1:
            if int(lst[i][0][j]) < int(lst[i][0][j+1]) and int(lst[i][0][j]) < int(lst[i-1][0][j]) and int(lst[i][0][j]) < int(lst[i+1][0][j]):
                counter += int(lst[i][0][j]) + 1
        elif j != 0 and i !=0 and i != len(lst)-1:
            if int(lst[i][0][j]) < int(lst[i][0][j-1]) and int(lst[i][0][j]) < int(lst[i-1][0][j]) and int(lst[i][0][j]) < int(lst[i+1][0][j]):
                counter += int(lst[i][0][j]) + 1
        elif j != 0 and j != len(lst[i][0])-1 and i != len(lst)-1:
            if int(lst[i][0][j]) < int(lst[i][0][j-1]) and int(lst[i][0][j]) < int(lst[i][0][j+1]) and int(lst[i][0][j]) < int(lst[i+1][0][j]):
                counter += int(lst[i][0][j]) + 1
        elif j != 0 and j != len(lst[i][0])-1 and i !=0:
            if int(lst[i][0][j]) < int(lst[i][0][j-1]) and int(lst[i][0][j]) < int(lst[i][0][j+1]) and int(lst[i][0][j]) < int(lst[i-1][0][j]):
                counter += inst(lst[i][0][j]) + 1

        elif j==0 and i==0:
            if int(lst[i][0][j]) < int(lst[i][0][j+1]) and int(lst[i][0][j]) < int(lst[i+1][0][j]):
                counter += int(lst[i][0][j]) + 1
        elif j==0 and i == len(lst)-1:
            if int(lst[i][0][j]) < int(lst[i][0][j+1]) and int(lst[i][0][j]) < int(lst[i-1][0][j]):
                counter += int(lst[i][0][j]) + 1
        elif j==len(lst[i][0])-1 and i == 0:
            if int(lst[i][0][j]) < int(lst[i][0][j-1]) and int(lst[i][0][j]) < int(lst[i+1][0][j]):
                counter += int(lst[i][0][j]) + 1
        elif j==len(lst[i][0])-1 and i == len(lst)-1:
            if int(lst[i][0][j]) < int(lst[i][0][j-1]) and int(lst[i][0][j]) < int(lst[i-1][0][j]):
                counter += int(lst[i][0][j]) + 1
        else:
            print("error",i,j)
print(counter)