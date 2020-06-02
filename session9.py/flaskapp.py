from flask import *
from pymongo import MongoClient

client = MongoClient("localhost:27017") #client = MongoClient() để nguyên cx mặc định localhost
db = client["c4e"] # or db = client.get_database("c4e")
users = db["customer"] # or users = db.get_collection("customer")

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Minh!"

@app.route("/aboutme/")
def aboutme():
    user = {"name": "HongMinh", "dob": "3.2.1998", "gender": "F", "address": "NCT", "nickname": "hihi"}
    return render_template("aboutme.html", user = user)

@app.route("/school")
def school():
    return redirect("https://mindx.edu.vn/")

@app.route("/bmi/<weight>/<height>")
def bmi(weight, height):
    # return f'{weight} {height}'
    weight = float(weight)
    height = float(height)
    res = weight/((height/100)**2) #biến weight, height khi được đưa vào sẽ chưa p là int/float ngay mà sẽ là str
    if res < 16:
        return "Severly underweight"
    elif res < 18.5:
        return "Underweight"
    elif res < 25:
        return "Normal"
    elif res <= 30:
        return "Overweight"
    else:
        return "Obese"

@app.route("/user/<username>")
def user(username):
    user_info = users.find_one({"name": username}) 

    #nếu muốn tìm theo 2 điều kiện thì sẽ viết {"name": username, "job": doctor}

    if user_info is not None:
        # return user_info["job"] + ", " + user_info["name"]
        return render_template(
            "user.html", 
            name = user_info["name"], 
            job = user_info["job"]
            ) 
        # xem o jinja template)
        # or return f'{user_info["job"]} {user_info["name"]}'
    else:
        return "User not found"


app.run(debug = True, port = 3000)
# nếu xóa debug = True thì sẽ k hiển thỉ lệnh print (nếu có), nếu có thì sửa lỗi dễ hơn và được load lại web 1 cách tự động
# port: cổng; để số bn cx đc
# k có cả 2 yếu tố vẫn chạy được
