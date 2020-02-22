k_number = 1
while k_number < 10:
    if k_number % 2 == 0: 
        k_number += 1  
        continue #khác gì với không có câu lệnh này ??
    print(k_number, 'is odd number')
    k_number += 1
k = 0
while k < 3:
    print('value of k is', k)
    k += 1
else: #khác gì so với khi bỏ?
    print('k is not less than 3 anymore')

