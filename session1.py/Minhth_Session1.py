
# Bài 1
born = int(input("Mời bạn nhập năm sinh: "))
years = 2020 - born
print(f"Tuổi của bạn là {years} tuổi")


# Bài 2
a= int(input("Nhập độ dài cạnh 1: "))
b = int(input("Nhập độ dài cạnh 2: "))
c = int(input("Nhập độ dài cạnh 3: "))
p = (a+b+c)/2
x = p*(p-a)*(p-b)*(p-c)
S = x**0.5
print(f"Diện tích tam giác là {S}")

# Bài 3
x = int(input("Nhập số nguyên x: "))
y = int(input("Nhập số nguyên y: "))
S = (x+y)/(2+x/y)
print(f"Giá trị biểu thức là {S}")