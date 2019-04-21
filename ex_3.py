right = []
left = []
my_list = ["La", "vie", "est", "belle"]
my_list.reverse()
length = len(my_list)
if length % 2 == 0:
    right += my_list[0:length//2]
    left += my_list[length//2:]
else:
    right += my_list[:length+1//2]
    left += my_list[length+1//2:]
print("right = ", right)
print("left = ", left)

