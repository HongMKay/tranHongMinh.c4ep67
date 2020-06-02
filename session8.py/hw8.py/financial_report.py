import requests
from bs4 import BeautifulSoup
from pyexcel import *

soup = BeautifulSoup(excel_content, "html.parser")

table_content = soup.find("table", {'id': 'tableContent'})


tr_content = table_content.find_all("tr")
data = []
for tr in tr_content:
    td_content = tr.find_all("td")
    info_value = []
    for td in td_content:
        info_value.append(str(td.string))

    for info in info_value:
        result = {
            'Danh mục': info_value[0],
            'Quý 4-2016': info_value[1],
            'Quý 1-2017': info_value[2],
            'Quý 2-2017': info_value[3],
            'Quý 3-2017': info_value[4]
        }
    data.append(result)

save_as(records=data, dest_file_name ='VNM_financial_report.xls')
