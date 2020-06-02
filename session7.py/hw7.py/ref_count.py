#bài 4
import pymongo
from bson import ObjectId
from matplotlib import pyplot

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = pymongo.MongoClient(mongo_uri, retryWrites = False)
db = client["c4e"]
count_refs = db['customers']

#count_ref: cách 1
a = count_refs.aggregate([
    { "$group": { "_id": "$ref", "Count": { "$sum": 1 } } },
    {"$sort": {"Count": -1}} #xếp theo từ cao descending order
    ])

#count ref: cách 2
num_of_customers = count_refs.find()
count_ads = 0
count_wom = 0
count_events = 0
for ref in num_of_customers:
    if ref['ref'] == 'ads':
        count_ads += 1
    elif ref['ref'] == 'wom':
        count_wom += 1
    else:
        count_events += 1
print('''Number of customers group by refs:
ads : {0}
wom : {1}
events : {2}
'''.format(count_ads, count_wom, count_events))

for group in a:
    print(group)
#Draw piechart
ref_count = [1134, 1939, 3902]
ref_name = ["Wom", "Ads", "Events"]
pyplot.pie(ref_count, labels= ref_name, autopct= "%.1f%%", shadow = True, explode=[0.2, 0.2, 0])

pyplot.title("Ref in customers: Events vs ads vs wom")
pyplot.axis("equal")

pyplot.show()

