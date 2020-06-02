# Asks users enter a number n and then calculates factorial of n: (1 * 2 * 3 *... *n)
n = input("Enter a number: ")
factorial = 1
if int(n) > 1:
    for i in range (1, int(n) +1):
        factorial = factorial * i
    print("Factorial of ",n,"is: ", factorial)