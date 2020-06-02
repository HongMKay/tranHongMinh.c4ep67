#Bài 9
def get_even_list(content):
    a = []
    for i in range(len(content)):
        if content[i] % 2==0:
            a.append(content[i])
        else:
            pass
    return a

#Bài 10
even_list = get_even_list([1, 2, 5, -10, 9, 6])
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")