#Bài 1
def chao_the_gioi():
    print("Hello world! "*3)

chao_the_gioi()
#Bài 2
def tinh_tong(a, b):
    print("Tổng là",a+b)

tinh_tong(2,3)

#Bài 3
from turtle import *
def draw_square(length, square_color):
    for i in range(4):
        speed(-1)
        color(square_color)
        forward(length)
        right(90)
    mainloop()
#Bài 4 
for i in range(40,100,10):
    left(17)
    penup()
    forward(i * 2)
    pendown()
    draw_square(i * 5, 'red')
#Bài 5
from turtle import *
def draw_star(x,y,length):
    penup()
    goto(x,y)
    pendown()
    for i in range(5):
        speed(-1)
        right(144)
        forward(length)
    mainloop()
#Bài 6 
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(300, 1000)
    draw_star(x, y, length)

#Bài 7
def remove_dollar_sign(content):
    a = content.replace("$","")
    return a

#Bài 8
string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")

#Bài 9
def get_even_list(content):
    a = []
    for i in range(len(content)):
        if content[i] % 2==0:
            a.append(content[i])
        else:
            pass
    return a

#Bài 10
even_list = get_even_list([1, 2, 5, -10, 9, 6])
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
#Bài 11
def is_inside(content1, content2 = [140, 60, 100, 200]):
    if content1[0] in range(140,241):
    # if content1[0] > 140 and content1[0] < 240:
        if content1[1] in range(60,261):
            result = True
        else:
            result = False
    else:
        result = False
    return result
#Bài 12
inside = is_inside([100,60])
if inside == False:
    print("Your function is correct")
else:
    print("Ooops, bugs detected")        







