from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    text = shapes[randint(0,3)]["text"]
    color = shapes[randint(0,3)]["color"]
    quiz_type = randint(0, 1) # 0 : meaning, 1: color   
    a =(text, color, quiz_type)
    return a

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

def mouse_press(x, y, text, color, quiz_type):
    # for i in range(len(shapes)):
        # inside = is_inside([x,y], shapes[i]["rect"])
        # if inside == True:
        #     choosen_text = shapes[i]["text"]
        #     choosen_color = shapes[i]["color"]
        # else:
        #     pass
    for i in range(len(shapes)):
        a = shapes[i]
        if is_inside([x,y], a["rect"]) == True:
            if a["text"] == shapes[randint(0,3)]["text"]:
                return True
            else:
                return False
        else:
            return False


