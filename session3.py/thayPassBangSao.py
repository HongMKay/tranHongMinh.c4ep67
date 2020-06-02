
# #Initial list
# res = []

# # Input lengths
# lengths = int(input())

# # Add element
# for i in range(lengths):
#     # Input elements
#     n = int(input())
#     res.append(str(n))
# res = [str(i) for i in res]

# print("".join(res))

# str = str(input())

# def check_str(str):
#     if len(str) < 3:
#         print(str)
#     else:
#         if str.endswith("ing") == True:
#             print(str,"ly")
#         else:
#             print(str,"ing")

# import array 


# arr = array.array('i', [1, 2, 3])
# n = int(input())
# new_arr = arr.append(n)
# new_arr = []
# for i in range(4):
#     new_arr.append(arr[i])
# print("The appended array:",new_arr)

#tìm số nhỏ nhất
# #Initial list
# res = []

# length = int(input())

# # Add element
# for i in range(length):
#     # Input elements
#     n = int(input())
#     res.append(n)

# min_num = res[0]
# for j in range(len(res)):
#     if res[0] > res[j]:
#         min_num= res[j]
# print(min_num)
    
    
# #Initial list
# res = []

# # Input length
# length = int(input())

# # Add element for res
# for i in range(length):
#     # Input elements
#     n = int(input())
#     res.append(n)

# new_res = []
# for num in res:
#     if num%5==0:
#         new_res.append(num)
# if len(new_res)==0:
#     print("[0]")
# else:
#     print(new_res)

random_float = float(input())

print("Formatted Number: %.2f%%"%(random_float*100))