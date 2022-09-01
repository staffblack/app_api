import json   
       
dictionary ={   
  "id": "04",   
  "name": "sunil",   
  "depatment": "HR"
}   
       
json_object = json.dumps(dictionary, indent = 4)   
print(json_object) 