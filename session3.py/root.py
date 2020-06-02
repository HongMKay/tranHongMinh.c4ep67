from getpass import getpass
username = 'mindx'
password = 'xdnim'

loop = True
count = 1 
while loop:
    count = count + 1 #(tương đương count +=1)
    if count == 5:
        print('spam vừa thôi')
        loop = False
    input_username = input('username? ')
    if input_username == username:
        input_password = getpass()
        
        # lop = True
        # count1 = 1
        # while lop:
        #     count1 +=1
        #     if count1 == 5:
        #         print('Biến đê')
        #         lop = False
        if input_password == password:
            print('welcome to mindx')
            loop = False
        else:
            print('Wrong password')
    else: 
        print('Wrong username')

# nếu muốn k show passwword thì dùng câu lệnh
# from getpass import getpass
# password = getpass()