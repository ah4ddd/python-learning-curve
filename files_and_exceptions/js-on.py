import json

dickionary = {"ahad": 20, "mia" : 23, "us": "we hate each other"}

jsonstring = json.dumps(dickionary)

print(type(jsonstring))

dickionary = '{"ahad": 20, "mia" : 23, "us": "we hate each other"}'

jsonstring = json.loads(dickionary)

print(type(jsonstring))
