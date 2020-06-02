ve 6 hinh long nhau
from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
count = 0
for i in range (3,8):
    for j in range (i):
        color(colors[count])
        forward(100)
        left(360/i)
    count += 1
mainloop()