## < taraf smte chap istade, > taraf samte rast istade!
state_1 = "<<<><<<<><<<<><<<<"
stage_2 = ""
for i in state_1:
    if state_1 == ">":
        state_1 = "<"
    stage_2 += state_1
    print(stage_2)
else:
    stage_2 += state_1
print(stage_2)




