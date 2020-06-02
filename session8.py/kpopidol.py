import requests
from bs4 import BeautifulSoup
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/", retryWrites = False)

db = client["c4e"]
customer_collection = db["kpop_idol"]

k_idol_content = requests.get("https://dbkpop.com/db/all-k-pop-idols?fbclid=IwAR3mq7Lx3E19LWWmhSZ3TChIOGT5K9enpgxDqUQU7tsaOkj5ls0cwp13l1c") #lấy ndung từ web nào

soup = BeautifulSoup(k_idol_content.text, "html.parser") #k_idol_content.text để chỉ lấy text cho đẹp
soup1 = soup.find("tbody")

tr_content = soup1.find_all("tr")

for tr in tr_content:
    td_content = tr.find_all("td")
    k_idol = []
    idol_dict = {}
    person = ["profile","stage_name","full_name","kor_name","kor_stage_name",'dob',"group", "country","second country","height","weight","birthplace","other group","former group","gender","position","instagram","twitter"]
    for td in td_content:
        k_idol.append(str(td.string))
    for i in range(len(person)):
        idol_dict[person[i]] = k_idol[i]
    
    customer_collection.insert_one(idol_dict)



    
