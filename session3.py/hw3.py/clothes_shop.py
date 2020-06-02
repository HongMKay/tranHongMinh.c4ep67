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