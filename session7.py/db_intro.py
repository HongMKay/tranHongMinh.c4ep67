import pymongo
from bson import ObjectId
from faker import Faker

fake = Faker()

client = pymongo.MongoClient("mongodb://localhost:27017/", retryWrites = False)

db = client["c4e"]
customer_collection = db["customer"]

# #cách thêm dữ liệu
new_data = []
for i in range(100):
    data = {
        "name": fake.name(),
        "age": fake.job(),
        "address": fake.address(),
        "phone": fake.phone_number()
    }
    new_data.append(data)

#thêm nhiều dữ liệu
customer_collection.insert_many(new_data) # kiểu dữ liệu bên ngoài là list, bên trong là dict


#thêm 1 dữ liệu
# customer_collection.insert_one({
#     "name": "Min",
#     "age": 50,
#     "address": "dong da"
# })
# # với lệnh này thì phải là 1 dict

#cách lấy dữ liệu
#READ DATA
data = customer_collection.find({"age": {"$lt": "18"}})
data1 = customer_collection.find_one({"_id": ObjectId('5e5520c3aeeca6941555bb7f')})
print(data1)
#tìm dữ liệu ghi cả key lẫn value
#{"$lt": "18"} dấu $ để đánh dấu biểu thức so sánh của mongodb
# lt = little than/ gt = greater than

#từ khóa find sẽ trả ra nhiều kqua ở 1 dạng dữ liệu tương tự list
#từ khóa để tìm 1 kết quả đầu tiên: find_one

#update data
customer_collection.update_one(
    {
        "_id": ObjectId('5e5520c3aeeca6941555bb7f')
    }, 
    {
        "$set": {
            "name": "Hihi"
        } #chỉ thay đổi name, các tphan khác giữ nguyên  
    }
)
#sẽ có nhiều keyword khác ngoài $set để thực hiện lệnh update

#delete
customer_collection.delete_one({
    "_id": ObjectId('5e5520c3aeeca6941555bb7f')
})

