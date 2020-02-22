teencode = {
    "ncl": "nói chung là",
    "cl": "củ lạc",
    "nl": "như là",
    "clgt": "củ lạc giòn tan",
    "cc": "con chó"
}

loop = True
while loop:
    a = input("Enter word you want to translate (Or type E to exit): ").strip()
    if a in teencode:
        print(a, "có nghĩa là ", teencode[a])
    elif a not in teencode and a == "E":
        print("Bói boi")
        loop = False
    else: 
        b = input("Từ này không có trong từ điển, bạn có muốn thêm nghĩa từ này hok? Yes or No ").lower()
    #lower là lệnh quy hết chữ thành chữ thường
    #strip() bỏ hết khoảng trắng ở đầu và cuối của chữ
        if b == "yes":
            c = input("Nghĩa: ")
            teencode[a] = c
            print("Bạn đã thêm thành công ")
        elif b == "no":
            print("Tui sẽ tìm hiểu sau nha ")
        else:
            print("Bói boi")

