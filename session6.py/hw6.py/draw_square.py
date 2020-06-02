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