quizzes = [
    {
        "question": "Tay có mấy ngón?",
        "choices":[
        "3 ngón", 
        "4 ngón", 
        "5 ngón", 
        "6 ngón"
        ],
        "right_ans": 2
    },
    {
        "question": "Nhện có mấy chân?",
        "choices":[
        "2 ngón", 
        "4 ngón", 
        "10 ngón", 
        "8 ngón"
        ],
        "right_ans": 3
    },
    {
        "question": "Rắm có thơm k?",
        "choices":[
        "Có", 
        "Éo"
        ],
        "right_ans": 1
    }
]

for k in range(len(quizzes)): #or for quiz in quizzes (cách nhanh hơn)
    if k < len(quizzes):
        score = 0
        print(f'Câu {k+1}. {quizzes[k]["question"]}')

        a = quizzes[k]['choices']
        for i in range (len(a)):
            print (f'{i+1}. {a[i]}')
        user_choice = int(input("Trả lời đê!!: ")) - 1 #bởi vì đã cộng 1 ở trên rồi
        if user_choice == quizzes[k]["right_ans"]:
            print("Sugoiiii")
            score +=1
        else:
            print("Oopsie :(")
        print()
    else:
        print(score, "Điểm bạn là: ")



