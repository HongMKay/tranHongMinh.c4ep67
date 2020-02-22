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

lis = [4,5,6,7,3,6,3,6,2,6,2,5]
output = []
for num in lis:
     if num%2==0:
        output.append(num)
print(output)
