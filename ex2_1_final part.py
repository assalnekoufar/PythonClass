# ## < samte chap , > samte rast, natije : <<><<><,<<<><<>,<<<<><>,<<<<<><,<<<<<<>
def checking(str):
    for i in range(len(str)-1):
        if str[i] == ">" and str[i+1] == "<":
            return i


counter = 0
state_1 = "<><<><<"
while checking(state_1) in range(len(state_1)):
        state_1 = state_1[:checking(state_1)] + "<>" + state_1[checking(state_1)+2:]
        counter += 1
        print(state_1)
print(counter)
