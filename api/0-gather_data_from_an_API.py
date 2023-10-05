#!/usr/bin/python3
# A Python script that, using REST API, for a given employee ID,
# returns information about his/her TODO list progress


import json
import requests
import sys

e_id = sys.argv[1]
api_url = f'https://jsonplaceholder.typicode.com/users/{e_id}/todos'
employee_detail = f'https://jsonplaceholder.typicode.com/users/{e_id}'

# Specific employee details
res = requests.get(employee_detail)
eData = res.json()
dataStr = json.dumps(eData)
dataObj = json.loads(dataStr)

for key in dataObj:
    if key == 'name':
        name = dataObj[key]

# TODO items for an employee with id 
response = requests.get(api_url)
data = response.json()
data_str = json.dumps(data)
data_obj = json.loads(data_str)
counter = 0
titleList = []

for index in range(len(data_obj)):
    for key in data_obj[index]:
        if key == 'title' and data_obj[index]['completed'] == True:
            counter += 1
            titleList.append(data_obj[index][key])

print(f'Employee {name} is done with tasks({counter}/{len(data_obj)}):')
for i in range(len(titleList)):
    print('\t', titleList[i])