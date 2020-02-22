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

# Asks users enter a number n and then calculates factorial of n: (1 * 2 * 3 *... *n)
n = input("Enter a number: ")
factorial = 1
if int(n) > 1:
    for i in range (1, int(n) +1):
        factorial = factorial * i
    print("Factorial of ",n,"is: ", factorial)

