# siz = [5, 7, 300, 90, 24, 50, 75]

# input(f"Hello my name is Kay and these are my sheep sizes {siz}")
# big1 = max(siz)
# ind = siz.index (big1)
# siz[ind]= 8
# input(f"Now my biggest sheep has size {big1} let's shear it")
# print(f"After shearing, here is my flock {siz}")
# print()

# month = ["MONTH 1:", 'MONTH 2:', "MONTH 3:"]
# for b in range (3):
#     input(month[b])
#     for i in range (0,7):
#             siz[i] += 50
#     input(f"One month has passed, now here is my flock {siz}")
#     if b < 2:
# # find the biggest sheep
#         big1 = max(siz)
#         ind = siz.index (big1)
#         siz[ind]= 8
#         input(f"Now my biggest sheep has size {big1} let's shear it")
#         print(f"After shearing, here is my flock {siz}")
#         print()

#     else:
#         c = sum(siz)
#         input(f"My flock has size in total: {c}")
#         d = c *2
#         input(f"I would get {c} * 2$ = {d}$")
# print()

import random
word = ['chair', 'table', 'sister', 'smile']

a = random.choice(word) 
li = list(a) #chuyển a từ str thành list
random.shuffle(li) #shuffle không áp dụng cho string mà phải là list
shuffled = ' '.join(li)
print(shuffled)

n = input("Your answer: ")
if n == a:
    print('Hura')
else:
    print('Oopsie a daisy')
print()

high_score = [44, 55, 34, 56, 30]
# # In ra THEO THỨ TỰ INDEX
a = len(high_score)
print("High score: ")
for i in range(1,a+1):
    print(i, end = '. ')
    print(high_score[i-1])

x = int(input("Enter your new score: "))
high_score.append(x)

a = len(high_score)
print("High score: ")
for i in range(1,a+1):
    print(i, end = '. ')
    print(high_score[i-1])

#In điểm từ cao đến thấp
count = 0
for count in range (2):
    high_score.sort(reverse=True)
    print("High score: ")
    for i in range(1,6):
        # print(i,".",high_score[i-1])
        print("{0}. {1}".format(i, high_score[i-1]))

    x = int(input("Enter your new score: "))
    high_score.append(x)
    count += 1

top5 = []
for z in range (6):
    b = max(high_score)
    top5.append(b)
    high_score.remove(b)
print("New high score:")   
for k in range(1,6):
    top5.sort(reverse=True)
    # print(k,".", top5[k-1])
    print("{0}. {1}".format(k,top5[k-1]))



