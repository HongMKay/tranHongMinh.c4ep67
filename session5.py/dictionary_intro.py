# person = ['Đức', 96, "Hà Nội", "Sơn La", "dev", False, True]
# Kiểu dữ liệu dictionary: {'Key': value (bất kì 1 loại value nào), 'Key': value}
# Không giới hạn số lượng cặp Key-value, không có index
# Key luôn phải độc nhất, khi 2 key giống nhau thì mọi thao tác sẽ lấy phần tử ở phía dưới cùng

person = {
    'name': "Đức", 
    "yob": 96, 
    "address": "Hà Nội"
}
# key = input()
# print(person[key])

person['gender'] = 'Male' #create tạo thêm 1 key

person['address'] = "Đà Lạt" #Update thay đổi giá trị trong dict

del person['yob'] #delete

print ("job" in person)
print("name" in person) #kiểm tra xem key có trong dict hay không

# classroom = {
#     'name': {"name of class": "C4E67", "name of place": "Thành công"},
#     'teacher': "Đức",
#     "students": ['Minh', "Linh", "Hoa", "Mai"],
#     "Schedule": "7pm Tue"
# }
# print(classroom['students'][0]) #coi như list
# print(classroom['name']['name of class']) # coi như new dict

# READ full dict without colon and brackets:
for key, value in person.items():
    print(key,value)


