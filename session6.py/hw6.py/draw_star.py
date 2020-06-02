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