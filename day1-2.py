import parser as p
lst = p.singleparse("input1")

window = []
j =2

while j < len(lst):
    window.append(int(lst[j]) + int(lst[j-1]) + int(lst[j-2]))
    j += 1
    


i = 1
c = 0
while i < len(window):
    if(window[i] > window[i-1]):
        c += 1
    i += 1
print(c)
