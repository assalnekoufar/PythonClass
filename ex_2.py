# we R using yes for + answers and no for - ones
standard = str(input("are you using SI system? --->"))
height = float(input("what is your height? --->"))
weight = float(input("what is your weight? --->"))
if standard == "Yes":
    BMI = height / (weight ** 2)
else:
    BMI = (height/(weight**2))*703
if BMI < 18.5:
    print("underweight")
elif 18.5 <= BMI <= 25:
    print("normal")
elif 25 <= BMI <= 30:
    print("overweight")
else:
    print("obesity")