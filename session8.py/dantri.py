import requests
from bs4 import BeautifulSoup
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/", retryWrites = False)

db = client["c4e"]
customer_collection = db["dantri"]

dantri_content = requests.get("https://dantri.com.vn/") #lấy ndung từ web nào

soup = BeautifulSoup(dantri_content.text, "html.parser")

#dantri_content.text để ra đoạn html
#"html.parser" cho b truyền kiểu dữ liệu nào, ngoài ra còn nhận xml, xhtml

div_content = soup.find("div", {"class": "xnano"})
ul_content = div_content.find("ul", {"class": "ul1 ulnew"}) #trả về 1 cái thẻ
# print(ul_content)

li_content = ul_content.find_all("li")  #in ra 1 cái list
# print(li_content) 
for li in li_content:
    # print(li.h4.a.string) #lệnh để lấy nguyên chữ ở thẻ a
    news_link = li.h4.a['href'] #để ra cái link. dùng a như 1 dictionary vì href là 1 attribute trong thẻ mở chứ không phải content của thẻ a nên k chấm được
#chấm được li.h4.a vì trong thẻ li có h4, trong thẻ h4 có thẻ a
    title = li.h4.a.string
    news_title = str(title).strip() #chuyển thành dạng string và strip để mất hết dấu cách 2 đầu
    customer_collection.insert_one({
        "link": news_link,
        "title": news_title
    })

 
