#wget --load-cookies=cookies.txt https://adventofcode.com/2021/day/8/input
import parser as p
from collections import Counter
lst = p.autoparse("input8")
for i in range(len(lst)):
    del lst[i][10]

counter = 0

for i in lst:
    mapp = [None]*7
    stop = True
    for j in i:
        if len(j) == 2:
            one = j

        if len(j) == 3:
            seven = j

        if len(j) == 4:
            four = j

    eight = "abcdefg"

    mapp[0] = [ch for ch in seven if ch not in one][0]

    for j in i:
        common_letters = Counter(j) & Counter(four+mapp[0])
        if len(j) == 6 and sum(common_letters.values())==5:
            nine = j
            mapp[6] = [ch for ch in j if ch not in (four+mapp[0])][0]
    
    for j in i:
        common_letters1 = Counter(j) & Counter(nine)
        common_letters2 = Counter(j) & Counter(one)
        if len(j) == 5 and sum(common_letters1.values())==5 and sum(common_letters2.values())==2: 
            three = j
            mapp[1] = [ch for ch in nine if ch not in three][0]

    mapp[4] = [ch for ch in eight if ch not in nine][0]

    for j in i:
        common_letters1 = Counter(j) & Counter(one)
        common_letters2 = Counter(j) & Counter(nine)
        if len(j) == 6 and sum(common_letters1.values())!=2 and sum(common_letters2.values())!=6: 
            six = j
            mapp[2] = [ch for ch in eight if ch not in six][0]

    for j in i:
        common_letters1 = Counter(j) & Counter(six)
        common_letters2 = Counter(j) & Counter(nine)
        if len(j) == 6 and sum(common_letters1.values())!=6 and sum(common_letters2.values())!=6: 
            zero = j
            mapp[3] = [ch for ch in eight if ch not in zero][0]
        
    mapp[5] = [ch for ch in eight if ch not in mapp][0]

    def check_number(input):
        common_three = Counter(input) & Counter(three)
        common_six = Counter(input) & Counter(six)
        common_nine = Counter(input) & Counter(nine)
        if len(input) == 2:
            return 1
        elif len(input) == 3:
            return 7
        elif len(input) == 4:
            return 4
        elif len(input) == 5 and sum(common_three.values()) == 5:
            return 3
        elif len(input) == 5 and mapp[2] in input:
            return 2
        elif len(input) == 5:
            return 5
        elif len(input) == 6 and sum(common_six.values())==6:
            return 6
        elif len(input) == 6 and sum(common_nine.values())==6:
            return 9
        elif len(input)==6:
            return 0
        elif len(input)==7:
            return 8
    counter += check_number(i[10])*1000 + check_number(i[11])*100 + check_number(i[12])*10 + check_number(i[13])
print(counter)