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