'''Import required modules'''
import json

overall = {
    'marks': {},
    'total': 0,
    'feedback': {}
}

marks = {}

feedback = {}

# --------------------------- Record ---------------------------
overall['marks'] = marks
overall['total'] = sum(sum(compo.values()) for compo in marks.values())
overall['feedback'] = feedback
print('------------------------- MARKS ------------------------------')
print(json.dumps(marks, indent=4))
print('----------------------- FEEDBACK -----------------------------')
print(json.dumps(feedback, indent=4))
print('--------------------------------------------------------------')
with open('../evaluate.json', 'w', encoding='utf-8') as f:
    json.dump(overall, f, indent=4)
