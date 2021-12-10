#wget --load-cookies=cookies.txt https://adventofcode.com/2021/day/10/input
import parser as p
lst = p.singleparse("input10")
lst2 = []

def get_score(token):
    result = 0
    for i in token:
        result = result*5
        if i == ")":
            result += 1
        elif i == "]":
            result += 2
        elif i == "}":
            result += 3
        elif i == ">":
            result += 4
    return result


for i in lst:
    line = []
    corrupt = False
    for j in i:
        if j == "(":
            line.append(")")
        elif j == "<":
            line.append(">")
        elif j == "[":
            line.append("]")
        elif j == "{":
            line.append("}")
        elif j == line[-1]:
            del line[-1]
        else:
            corrupt = True
            break
    if not corrupt:
        lst2.append(i)

def makescore(lst):
    score = []
    for i in lst:
        line = []
        for j in i:
            if j == "(":
                line.append(")")
            elif j == "<":
                line.append(">")
            elif j == "[":
                line.append("]")
            elif j == "{":
                line.append("}")
            elif j == line[-1]:
                del line[-1]
            else:
                print("error2")
        line.reverse()
        score.append(get_score(line))
    return score

score = makescore(lst2)

score.sort()
print(score[len(score)//2])