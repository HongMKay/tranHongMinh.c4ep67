# def calc(a, b, operator):
#     if operator == "+":
#         result = a + b #hạn chế của print là nó chỉ hiện ra ở cửa sổ trên visual
#     elif operator == "-":
#         result = a - b
#     elif operator == "*":
#         result = a * b
#     elif operator == "/":
#         result= a / b 
    
#     return result #đến return là toàn bộ đoạn code sau bị dừng lại

# #function: là 1 chương trình con chạy trong 1 ctrinh lớn
# print(__name__) #name là main khi nó là chạy ở file chính chủ
# if __name__ == "__main__":
#     a = calc(5, 4, "*")
#     print(a)

def me(a,b):
    print(a,b)

lst = [1, "hey"]
me(*lst)