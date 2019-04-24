height = float(input("what is your height(m) ? --->"))
weight = float(input("what is your weight(kg) ? --->"))
BMI = height/(weight**2)

if BMI < 18.5:
    print("underweight")
elif 18.5 <= BMI <= 25:
    print("normal")
elif 25 <= BMI <= 30:
    print("overweight")
else:
    print("obesity")
