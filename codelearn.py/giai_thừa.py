#in chữ số cuối cùng khác 0 của giai thừa

def lastDigitDiffZero(n):
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    a = str(factorial)[::-1]
    for k in a:
        if k == "0":
            pass
        else:
            return k
            break

        
    

print(lastDigitDiffZero(5))