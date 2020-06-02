import requests
from bs4 import BeautifulSoup
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/", retryWrites = False)

db = client["c4e"]
customer_collection = db["kpop_idol"]

k_idol_content = requests.get("https://dbkpop.com/db/all-k-pop-idols?fbclid=IwAR3mq7Lx3E19LWWmhSZ3TChIOGT5K9enpgxDqUQU7tsaOkj5ls0cwp13l1c").text #lấy ndung từ web nào

soup = BeautifulSoup(k_idol_content.text, "html.parser")
table = soup.find("tbody")
tr_content = table.find_all("tr")
for tr in tr_content:
    td_content = tr.find_all("td")
    info_value = []
    for td in td_content:
        info_value.append(td.string)
        idol_dict = {
            "stage_name": info_value[1],
            "full_name": info_value[2],
            'k_name': info_value[3]
        }

customer_collection.insert_one(idol_dict)