high_score = [44, 55, 34, 56, 30]
# # In ra THEO THỨ TỰ INDEX
a = len(high_score)
print("High score: ")
for i in range(1,a+1):
    print(i, end = '. ')
    print(high_score[i-1])

x = int(input("Enter your new score: "))
high_score.append(x)

a = len(high_score)
print("High score: ")
for i in range(1,a+1):
    print(i, end = '. ')
    print(high_score[i-1])

#In điểm từ cao đến thấp
count = 0
for count in range (2):
    high_score.sort(reverse=True)
    print("High score: ")
    for i in range(1,6):
        # print(i,".",high_score[i-1])
        print("{0}. {1}".format(i, high_score[i-1]))

    x = int(input("Enter your new score: "))
    high_score.append(x)
    count += 1

top5 = []
for z in range (6):
    b = max(high_score)
    top5.append(b)
    high_score.remove(b)
print("New high score:")   
for k in range(1,6):
    top5.sort(reverse=True)
    # print(k,".", top5[k-1])
    print("{0}. {1}".format(k,top5[k-1]))
