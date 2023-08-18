'''Import required modules'''
from main import *
import json

overall = {
    'marks': {},
    'total': 0,
    'feedback': {}
}

marks = {}

feedback = {}

def analyser(func, *args):
    global marks, feedback
    lut = {}
    calls = {}
    f1 = open(f'out/{func.__name__}.txt', 'r',
              encoding='utf-8').readlines()[2:]
    marks[f'{func.__name__}'] = 0
    if func(lut, calls, *args) == int(f1[0].split(':')[1]):
        marks[f'{func.__name__}'] += 0.5
    else:
        feedback[f'{func.__name__}'] = 'wrong answer'
        return
    if len(lut) == int(f1[1].split(':')[1]):
        marks[f'{func.__name__}'] += 0.5
    else:
        feedback[f'{func.__name__}'] = 'wrong lookup'
        return
    if sum(calls.values()) == int(f1[2].split(':')[1]):
        marks[f'{func.__name__}'] += 0.5
    else:
        feedback[f'{func.__name__}'] = 'wrong calls'
        return


analyser(factorial, 10)
analyser(fibonacci, 40)
analyser(nCr, 13, 4)
analyser(ackermann, 3, 5)

# --------------------------- Record ---------------------------
overall['marks'] = marks
overall['total'] = sum(compo for compo in marks.values())
overall['feedback'] = feedback
print('------------------------- MARKS ------------------------------')
print(json.dumps(marks, indent=4))
print('----------------------- FEEDBACK -----------------------------')
print(json.dumps(feedback, indent=4))
print('--------------------------------------------------------------')
with open('../evaluate.json', 'w', encoding='utf-8') as f:
    json.dump(overall, f, indent=4)
