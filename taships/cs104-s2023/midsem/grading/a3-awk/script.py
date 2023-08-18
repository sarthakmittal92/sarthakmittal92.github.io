import os
import json

overall = {
    "data": []
}

data = []

def remove_emptylines(Lines):
    Lines = filter(None, (line.rstrip() for line in Lines))
    return list(Lines)

os.system("rm TestCase1/output.txt")
#------------------------------test case 1---------------------------
msg = "Correct output."
total = 1
result = {
      "testid": "1",
      "status": "success",
      "score": 0,
      "maximum marks" : 1,
      "message": ""
    }

os.system("awk -f users.awk TestCase1/sample.txt > TestCase1/output.txt")
file1 = open('TestCase1/expected_output.txt', 'r')
Lines1 = remove_emptylines(file1.readlines())
file2 = open('TestCase1/output.txt', 'r')
Lines2 = remove_emptylines(file2.readlines())

if len(Lines1) < len(Lines2) :
    total = 0
    msg = "Wrong output, Your output genrates some extra lines"
elif len(Lines1) > len(Lines2) :
    total = 0
    msg = "Wrong output, Some statments are missing"
else :
    for i in range(len(Lines1)) :
        if Lines1[i].strip() != Lines2[i].strip() :
            total = 0
            msg = "Wrong output, Expected statment : '" + Lines1[i].strip() + "' Your output : '" + Lines2[i].strip() + "'"
            break
    
result["testid"] = 1
result["score"] = total
result["message"] = msg

data.append(result.copy())
os.system("rm TestCase1/output.txt")


#------------------------------test case 2---------------------------
msg = "Correct output."
total = 1
result = {
      "testid": "2",
      "status": "success",
      "score": 0,
      "maximum marks" : 1,
      "message": ""
    }

os.system("awk -f users.awk TestCase2/sample.txt > TestCase2/output.txt")
file1 = open('TestCase2/expected_output.txt', 'r')
Lines1 = remove_emptylines(file1.readlines())
file2 = open('TestCase2/output.txt', 'r')
Lines2 = remove_emptylines(file2.readlines())

if len(Lines1) < len(Lines2) :
    total = 0
    msg = "Wrong output, Your output genrates some extra lines"
elif len(Lines1) > len(Lines2) :
    total = 0
    msg = "Wrong output, Some statments are missing"
else :
    for i in range(len(Lines1)) :
        if Lines1[i].strip() != Lines2[i].strip() :
            total = 0
            msg = "Wrong output, Expected statment : '" + Lines1[i].strip() + "' Your output : '" + Lines2[i].strip() + "'"
            break
    
result["testid"] = 2
result["score"] = total
result["message"] = msg

data.append(result.copy())
os.system("rm TestCase2/output.txt")

## Dumping the result
overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
    json.dump(overall,f,indent=4)

