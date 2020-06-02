#Bài 11
def is_inside(content1, content2 = [140, 60, 100, 200]):
    if content1[0] in range(140,241):
    # if content1[0] > 140 and content1[0] < 240:
        if content1[1] in range(60,261):
            result = True
        else:
            result = False
    else:
        result = False
    return result

#Bài 12
inside = is_inside([100,60])
if inside == False:
    print("Your function is correct")
else:
    print("Ooops, bugs detected")        







