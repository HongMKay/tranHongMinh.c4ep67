# list: mảng, array


places = ["Bãi biển", "Bệnh viện", "Đại sứ quán", "Khách sạn"]   #  initialize: khởi tạo list

new_place = input("enter new place pls ")
places.append(new_place) #create

places.index("Bệnh viện") #tìm được index của value
print(places.index("Bệnh viện"))

places[2] = "Tiểu sứ quán" #update

#Cách delete1 by index
places.pop(2) #delete phần tử mang index 2, nếu k điền index nào sẽ tự động xóa value cuối cùng
#Cách delete2 by value
places.remove("Khách sạn")

temp = places[0] #đổi vị trí biến
places[0] = places[1]
places[1] = temp

for i in range (len(places)): #len viết tắt cho độ dài length
    print(places[i])

# print(places) #read

#  4 thao tác làm với kiểu dữ liệu list 
# C: create, R: read, U: update, D: delete
# nameList = ["value", "value", "value"]
# index          0        1        2