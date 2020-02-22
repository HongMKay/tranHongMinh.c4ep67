import random #hoặc là from random import randint (dùng cách này thì khi muốn dùng hàm randint thì chỉ cần viết rand())
from calc import calc
#from (tên file) import (tên hàm)

score = 0

while True:
    rand = random.randint(0, 9)
    sai_so = random.randint(-1,1)
    operator = ["+", "-", "*", "/"]
    operator = operator[random.randint(0,3)]
    math = calc(rand, rand, operator)
    result = math + sai_so
    print("{} {} {} = {}".format(rand, operator, rand, result))
    user = input("y/n? ").lower()
    if result == math:
        if user == "y":
            score += 1
            print("Your score is:",score)
        else:
            score = 0
    else:
        if user == "n":
            score += 1
            print("Your score is:",score)
        else:
            score = 0

print('')
