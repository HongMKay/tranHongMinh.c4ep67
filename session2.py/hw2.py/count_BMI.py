x1 = int(input("Your height (cm): "))
y = int(input("Your weight: "))
x = x1/100
bmi = y/(x*x)
if bmi < 16:
    print("Severly underweight")
elif bmi >= 16 and bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal")
elif bmi >= 25 and bmi <= 30:
    print("Overweight")
else:
    print("Obese")


