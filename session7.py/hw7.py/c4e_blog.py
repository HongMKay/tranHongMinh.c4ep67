import pymongo
from bson import ObjectId
from matplotlib import pyplot
#Bài 3
client = pymongo.MongoClient("mongodb://admin:admin@ds021182.mlab.com:21182/c4e", retryWrites = False)
db = client["c4e"]

my_post = db["posts"]

my_post.insert_one({
    "title": "Tình hình dịch bệnh ngày 26/2",
    "author": "Trần Hồng Minh",
    "content": "Trích từ 'Troll Sinh Viên'. Theo nguyện vọng của tổng lãnh sự Hàn Quốc cũng như công dân nước bạn, thì UBND Thành phố Đà Nẵng, 23h55 đêm qua đã tiễn đoàn khách từ thành phố Daegu đã cùng hơn 200 người khác khởi hành về nước. Tuy nhiên, có thể là do cảm nhận được tình hình dịch bệnh tại quê nhà hoặc đã cảm nhận được vị ngon của bánh mì, nên 2 người Hàn Quốc đã xin được ở lại Đà Nẵng để cách ly tiếp và không đưa ra bất kỳ yêu cầu nào về khách sạn cũng như đồ ăn =)) Còn nói về khoản chơi đẹp thì Việt Nam ta lúc nào cũng là nhất, chi phí chuyến bay được bên mình chi trả hoàn toàn, đã thế còn bố trí tiếp viên người Hàn để công dân nước bạn đỡ có cảm giác lạc lõng, bơ vơ. Ngay sau đó, Tổng lãnh sự Hàn Quốc Ahn Minsik đã gửi lời cảm ơn sâu sắc tới Chính phủ Việt Nam và công nhận những động thái của nước ta là đúng đắn trong tình thế đại dịch Corona đang diễn biến hết sức khó lường. ---Mong các bạn học viên của Mindx luôn mạnh khỏe nhé---"
})

data = my_post.find_one({"author": "Trần Hồng Minh"})