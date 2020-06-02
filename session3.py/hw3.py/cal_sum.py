#cách 1
n = input('Enter a list of numbers, separated by ",": ').split()
sum = 0
for i in n:
    sum = sum + int(i)
print("Sum of the entered numbers: ",sum)

#cách 2
sum_mer = []
for i in n:
    sum_mer.append(int(i))
print(sum(sum_mer)) 