def in_ra(content):
# def + tên hàm (khác tên biến ở chỗ tên hàm thường là động từ)
    print(content)
# giải nghĩa: def = đang khai báo 1 function mà mỗi khi muốn function đấy chạy thì nó sẽ chạy qua đoạn code print

in_ra("haha") #gọi hàm, call function
in_ra("hong")
in_ra("hoy")

def greeting(name, age):
    print(f"hi, my name is {name}, im {age} years old")
greeting("Minh",10)

def add(a,b):
    total = a+b
    #total = a +b: biến total chỉ dùng đc bên trong function add
    return total #từ khóa giúp trả GIÁ TRỊ CỦA biến bên trong hàm ra ngoài chứ KHÔNG PHẢI TRẢ BIẾN TOTAL
#print(total) => k in đc do biến total k tồn tại bên ngoài
a = add(2,1) #vẫn p gán vào 1 biến khác để hứng giá trị đc trả ra
print(a)

#variable scope: (phạm vi của biến) nếu khai báo biến trong function thì chỉ dùng đc biến đấy ở BÊN TRONG FUNCTION ĐÓ, bên ngoài k gọi được

# có 2 kiểu hàm: 
# 1. fruit_full function: hàm có trả kqua về, đc nhận diện qua từ khóa return hoặc có gán gtri trả về vào 1 biến
# 2. hàm k có kqua trả về (giả sử như hàm print - k cần phải gán vào biến nào cả, nó chỉ hiện ra màn hình)