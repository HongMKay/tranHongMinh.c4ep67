def pagesNumbering(n):
    if n <= 9:
        return n
    else:
        sum = 9
        for i in range(10, n+1):
            if i <=99:
                sum += 2
            elif i > 99 and i <= 999:
                sum + = 3