#wget --load-cookies=cookies.txt https://adventofcode.com/2021/day/10/input
import parser as p
lst = p.singleparse("input10")

counter = 0
def get_score(token):
    if token == ")":
        return 3
    elif token == "]":
        return 57
    elif token == "}":
        return 1197
    elif token == ">":
        return 25137
    else:
        print("error")

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
            counter += get_score(j)
            break
print(counter)