'''Import required modules'''
import json
import cv2
import numpy as np

overall = {
    'marks': {},
    'total': 0,
    'feedback': {}
}

def calc():
    img1 = cv2.imread('../plot.png',0)
    img2 = cv2.imread('./plot.png',0)
    res = cv2.absdiff(img1,img2)
    res = res.astype(np.uint8)
    return np.count_nonzero(res) * 100 / res.size

marks = {}

feedback = {}

p = calc()
if p < 30.0 and p != 0:
    marks['plot'] = 3
    feedback['plot'] = 'success'
else:
    marks['plot'] = 0
    feedback['plot'] = 'failed'

# --------------------------- Record ---------------------------
overall['marks'] = marks
overall['total'] = sum(compo for compo in marks.values())
overall['feedback'] = feedback
print('------------------------- MARKS ------------------------------')
print(json.dumps(marks, indent=4))
print('----------------------- FEEDBACK -----------------------------')
print(json.dumps(feedback, indent=4))
print('--------------------------------------------------------------')
print(f'Total: {sum(compo for compo in marks.values())}/3')
print('--------------------------------------------------------------')
with open('../evaluate.json', 'w', encoding='utf-8') as f:
    json.dump(overall, f, indent=4)
