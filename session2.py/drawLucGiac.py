#ve 5 hinh long nhau
# from turtle import *
# for i in range (6):
#     forward(100)
#     left(60)
# for l in range (5):
#     forward(100)
#     left(72)
# for r in range (4):
#     forward(100)
#     left(90)
# for z in range (3):
#     forward(100)
#     left(120)


# mainloop()
#ve 4 hinh binh hanh
# from turtle import *
# speed(-1)
# left(30)
# forward(100)
# right(60)
# forward(100)
# right(120)
# forward(100)
# right(60)
# forward(200)
# left(60)
# forward(100)
# left(120)
# forward(100)
# left(60)
# forward(100)
# left(30)
# forward(100)
# left(60)
# forward(100)
# left(120)
# forward(100)
# left(60)
# forward(200)
# right(60)
# forward(100)
# right(120)
# forward(100)
# right(60)
# forward(100)


# mainloop()

# for item in range(0,20):
#     print(item, sep=' ', end= ' ')

# n = int(input('Enter the number: '))
# for i in range(0,n):
#     print(i, sep=' ', end= " ")

# for i in range (0,20):
#     if i%2==0:
#         print(1, end= ' ')
#     else:
#         print(0, end= ' ')

# a = int(input('Enter the number: '))
# for a in range (0,a):
#     if a%2==0:
#         print(1, end= ' ')
#     else:
#         print(0, end =' ')

# for i in range (1,10):
#     for j in range (1,10):
#         a= i*j
#         if a > 9:
#             print(a, end =' ')
#         else:
#             print(a, end='  ')
#     print()
        
# n = int(input('Enter the number: '))
# for i in range (1, n+1):
#     for j in range (1, n+1):
#         a= i*j
#         if a > 9:
#             print(a, end =' ')
#         else:
#             print(a, end='  ')
#     print()

# for i in range (0,10):
#     for j in range (0,10):
#         if j%2==0:
#             print(1, end=' ')
#         else:
#             print(0, end=" ")
#     print()

a = int(input('Enter the number: '))
for i in range (0,a+1):
    for j in range (0,a+1):
        if i%2==0:
            if j%2==0:
                print(1, end=' ')
            else:
                print(0, end=" ")
        else: 
            if j%2==0:
                print(0, end=' ')
            else:
                print(1, end=" ")


    print()

