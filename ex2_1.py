## < samte chap , > samte rast, natije : <<><<><
state_1 = "<><<><<"
lst = []
i = -1
for c in state_1:
    lst.append(c)
    i += 1
    if i > 0 and lst[i-1] == ">" and lst[i] == "<":
        lst[i-1] = "<"
        lst[i] = ">"

print(lst[:])
