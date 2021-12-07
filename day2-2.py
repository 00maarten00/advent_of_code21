import parser as p
lst = p.autoparse("input2")

a = 0
h =0
v = 0
for i in lst:
    if i[0] == "forward":
        h += int(i[1])
        v += a*int(i[1])
    elif i[0] == "up":
        a -= int(i[1])
    elif i[0] == "down":
        a += int(i[1])
    else:
         print("ERROR")
print(h*v)
