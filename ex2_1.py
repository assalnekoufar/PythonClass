# ## < samte chap , > samte rast, natije : <<><<><,<<<><<>,<<<<><>,<<<<<><,<<<<<<>
state_1 = "<><<><<"
state_1_list = []
lst = []
i = -1
counter = 0
state_2 = ""
for w in state_1:
    state_1_list.append(w)
for c in state_1_list:
    lst.append(c)
    i += 1
    if i > 0 and state_1_list[i-1] == ">" and state_1_list[i] == "<":
        lst[i-1] = "<"
        lst[i] = ">"
        counter += 1
for n in lst:
    state_2 += n
print(state_2)
print(counter)


