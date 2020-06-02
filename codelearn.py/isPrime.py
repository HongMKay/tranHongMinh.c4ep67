def isPrime(n):
    if n < 0:
        pass
    elif n == 0:
        return False
    else:
        for i in range(2,n,1):
            print(i)
            if n%i==0:
                return False
        else:
            return True

print(isPrime(133))





