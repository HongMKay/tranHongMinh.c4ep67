#tìm ước chung nguyên tố lớn nhất
def greatestCommonPrimeDivisor(a, b):
    if b == 0:
        res = []
        for i in range(2,a+1):
            while a %i == 0:
                a /= i
                res.append(i)
        if len(res) > 0:
            return max(res)
        else:
            return -1
    else:
        return greatestCommonPrimeDivisor(b,a%b)



res = greatestCommonPrimeDivisor(12,18)
print(res)