# Python program to read
# json file


import json

# Opening JSON file
f = open('employee.json')

# returns JSON object as
# a dictionary
data = json.load(f)
lst = []
# Iterating through the json
# list
for i in data['employees']:
  lst.append(i)
  
print(lst)  
# Closing file
f.close()
