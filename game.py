import random

secret_number = random.randint(1, 100)

def check(i):
    if i > secret_number:
        return ">"
    elif i < secret_number:
        return "<"
    else:
        return "="

def show_message(n):
    messages = {">": "it is greater than your secret number",
                "<": "it is lesser than your secret number",
                "=": "it is equal to your secret number"}

    print(messages[n])

check_res = 'whatever'
while check_res != "=":
    number = int(input("enter your number --->"))
    check_res = check(number)
    show_message(check_res)

