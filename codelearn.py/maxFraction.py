def maxFraction(numerators, denominators):
    res = []
    for i in range(len(numerators)):
        a = float(numerators[i]/ denominators[i])
        res.append(a)
    return res.index(max(res))

print(maxFraction([1,2,3],[4,5,6]))

