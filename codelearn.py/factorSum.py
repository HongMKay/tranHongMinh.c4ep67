def factorSum(n):
    sumOfFactorPrime = 0
    temp_n = n
    for i in range(2, n + 1):
        while n % i == 0:
            n /= i
            sumOfFactorPrime += i
    if sumOfFactorPrime == temp_n:
        return sumOfFactorPrime
    else:
        return factorSum(sumOfFactorPrime)  

a = factorSum(24)
print(a)