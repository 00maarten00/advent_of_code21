import parser as p
lst = p.singleparse("input1")


i = 1
c = 0
while i < len(lst):
    if(int(lst[i]) > int(lst[i-1])):
        c += 1
    i += 1
print(c)
