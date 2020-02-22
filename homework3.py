# ve 6 hinh long nhau
# from turtle import *
# colors = ['red', 'blue', 'brown', 'yellow', 'grey']
# count = 0
# for i in range (3,8):
#     for j in range (i):
#         color(colors[count])
#         forward(100)
#         left(360/i)
#     count += 1
# mainloop()


# lis = [4,5,6,7,3,6,3,6,2,6,2,5]
# output = []
# for num in lis:
#      if num%2==0:
#         output.append(num)
# print(output)

# n = input('Enter a list of numbers, separated by ",": ').split()
# even_number = []
# for i in n:
#     if int(i)%2==0:
#         even_number.append(int(i))
#     else:
#         pass
# print(even_number)

# n = input('Enter a list of numbers, separated by ",": ').split()
# sum = 0
# for i in n:
#     sum = sum + int(i)
# print("Sum of the entered numbers: ",sum)

# sum_mer = []
# for i in n:
#     sum_mer.append(int(i))
# print(sum(sum_mer)) 

# dis = ["ST", "BD", "BTL", "CG", "DD", "HBT"]
# pop = [150300, 247100, 333300, 266800, 420900, 318000]
# max_pop = max(pop)
# min_pop = min(pop)
# a = pop.index(max_pop)
# b = pop.index(min_pop)

# print("Index of max pop district: ",a)
# print("Index of min pop district: ",b)
# print("Max pop district: ",dis[a])
# print("Min pop district: ",dis[b])

# area = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]

# mat_do = []
# for i in range (6):
#     n = pop[i]/area[i]
#     mat_do.append(int(n))
# print("Mật độ dân số của các quận: ",mat_do)
# ave_mdo = sum(mat_do)/len(dis)
# print("Mật độ dân cư trung bình: ", ave_mdo)

n = str(input("Welcome to our shop, what do you want (C, R, U, D)? ")).lower()
items = ["T-Shirt", "Sweater"]
if  n == "r" :
    print("Our items: ")
    for item in items:
        print(item, end=' ')

elif n == "c":
    m = str(input("Enter new item: "))
    items.append(m)
    print("Our items: ",', '.join(items)) #in k còn ngoặc list

elif n == "u":
    new_pos = int(input("Update position? "))
    new_it = input("New item? ")
    items.insert(new_pos,new_it)
    print("Our items: ",items)
elif n == "d":
    dele = int(input("Delete position? "))
    if dele >= len(items):
        print("Sory we don't have that much of item")
    else:
        items.pop(dele)
        print("Our items: ",items)
else:
    print("Moi nhap lai")








