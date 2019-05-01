def calculation(n1, n2, operator="+"):
    if operator == "**":
        res = n1 ** n2
    elif operator == "-":
        res = n1 - n2
    else:
        res = n1 + n2
    return res


number_1 = int(input("enter your first number--->"))
number_2 = int(input("enter your second number--->"))
operation = input("enter your desired operator--->")
print((calculation(number_1, number_2, operation)))

