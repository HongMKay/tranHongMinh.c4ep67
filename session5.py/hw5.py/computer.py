#PART 1
#Câu 1
dic = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}
# câu 2
print("Số lượng Macbook có trong kho là: ", dic["MACBOOK"])
#câu 3
a = input("Enter name you want to check quantity (HP/DELL/MACBOOK/ASUS): ").upper()
print("The quantiy of that branch is: ",dic[a])
#PART 2
#Câu 4
dic["TOSHIBA"] = 10
#Câu 5
user_add_type = input("Enter new type: ").upper()
user_add_number = int(input("Enter number: "))
dic[user_add_type] = user_add_number
#câu 6
dic["DELL"] += 10
dic["MACBOOK"] = 2
#PART 3
#câu 7
print("List of all computers:")
for key,value in dic.items():
    print(key,":",value)
# câu 8
value = dic.values()
list_value = list(value)
sum = 0
for i in range(len(list_value)):
    sum += list_value[i]
print("Tổng số máy là: ",sum)
#câu 9
dic["FUJITSU"] = 15
dic["ALIENWARE"] = 5
#câu 10
print("List of all computers:")
for key,value in dic.items():
    print(key,":",value)
#PART 4
#câu 11
price = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 12000,
    "ASUS": 400,
    "ACER": 350,
    "TOSHIBA": 600,
    "FUJITSU": 900,
    "ALIENWARE": 1000
}
user_price = int(input("Enter price for the new type you just entered: "))
price[user_add_type] = user_price
#Câu 12
print("Price ASUS: ",price["ASUS"],"$")
#câu 13
b = input("Enter branch you want to know price: ").upper()
print("The price is: ",price[b],"$")
#PART 5
#câu 14
p = price["ASUS"] *5
print("Price of 5 ASUS is: ",p,"$")
#câu 15
buy_com = input("Enter the name of computer you want to buy: ").upper()
buy_num = int(input("Enter the quantity: "))
total = price[buy_com] * buy_num
print("Total price: ",total,"$")
#câu 16
dic["ASUS"] -= 5
dic[buy_com] -= buy_num
print(dic)
#Câu 17
print("{0}:{1}".format(buy_com, buy_num))
print(dic)
#Part 6
#câu 18 +19
total_value = 0
for key in dic.keys():
    sum_1_branch = dic[key] * price[key]
    total_value += sum_1_branch
    print(f"Total value of {key} is {sum_1_branch}$")
print()
print(f"Total value of all computers: {total_value}$")









