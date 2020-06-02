# row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('','','')
# row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
# row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Yui Hatano', 'Japanese')
# row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'Sunny Leone', 'Canada')
# row_5 = row_1

# print(row_1)
# print(row_2)
# print(row_3)
# print(row_4)
# print(row_5)

# print('+ {:-<6} + {:-^15} + {:->10} +\n'.format('', '', '') + '| {:<6} | {:^15} | {:>10} |\n'.format('ID', 'Ho va ten', 'Noi sinh') + '| {:<6} | {:^15} | {:>10} |\n'.format('123', 'Yui Hatano', 'Japanese') + '| {:<6} | {:^15} | {:>10} |\n'.format('6969', 'Sunny Leone', 'Canada') + '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', ''))


# if 'how kteam free education'.endswith('n', 0, 9):
#     print('yay')
# else:
#     print('neh')

# if 'how kteam free education'.startswith('k', 4):
#     print('ú ù')
# else: 
#     print('ehh')

# s = 'aaaAAaaaooaaneu mot Ngay naO Doaaaaaaa'
# s = s.lower().strip('a').lstrip('ao').title()
# print(s)

# s = 'aaaaaaaAAAAAaaa//123123//000000//&&TTT%%abcxyznontqfadf'
# code = s.split('&&')[-1].split('%%')[0]
# print(code)

# Kteam = [1, 2, 3]
# print(Kteam.index(2))

# lst = list()
# lst
# []
# lst.pop

# lst = [[1, 2], ['abc', 'def']]
# lst.sort()
# print(lst)

# lis = [4,5,6,7,3,6,3,6,2,6,2,5]
# output = []
# for num in lis:
#      if num%2==0:
#         output.append(num)
# print(output)

# from math import sqrt

# a = int(input())
# b = int(input())
# c = int(input())

# r = b**2 - 4*a*c

# if a!= 0:
#     if r > 0:
#         i = sqrt(r)
#         A = (- b - i)/2*a
#         B = (- b + i)/2*a
#         print("There are 2 roots: %.6f and %.6f"%(A,B))
#     elif r == 0:
#         C = (- b)/ 2*a
#         print("There is one root: %.6f"%(C))
#     else:
#         print("No roots, discriminant < 0")
# else: 
#     if b!= 0:
#         D = (-c)/b
#         print("There is one root: %.6f"%(D))
#     else:
#         print("No roots, discriminant < 0")


# # method to compute gcd ( recursion ) 
# #tìm ước chung lớn nhất
# def hcfnaive(a,b): 
# 	if(b==0): 
# 		return a 
# 	else: 
# 		return hcfnaive(b,a%b) 

# a = 60
# b= 48

# # prints 12 
# print ("The gcd of 60 and 48 is : ",end="") 
# print (hcfnaive(60,48)) 

str = str(input())

def over_3_char_str(str):
        output = []
        new_str = str.split()
        for i in new_str:
                if len(i) > 3:
                        output.append(i)
                else:
                        pass
        print("".join(output))

over_3_char_str(str)
