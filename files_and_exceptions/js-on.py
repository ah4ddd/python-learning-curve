import json

data = {"name": "Ahad", "score": 1500}

json_string = json.dumps(data)

print(json_string)
print(type(json_string))
