#!/usr/bin/python3

import json
import requests
import sys

e_id = sys.argv[1]
api_url = f'https://jsonplaceholder.typicode.com/users/{e_id}/todos'
employee_detail = f'https://jsonplaceholder.typicode.com/users/{e_id}'

# Fetch specific employee details
res = requests.get(employee_detail)
eData = res.json()
username = eData.get('username', '')

# Initialize an empty list to store task data
tasksList = []

# Fetch TODO items for the employee with the given ID
response = requests.get(api_url)
data = response.json()

# Create a list of dictionaries for each task
for item in data:
    task = item.get('title', '')
    status = item.get('completed', False)
    tasksList.append({'task': task, 'completed': status, 'username': username})

dataSet = {e_id: tasksList}

# Write the data to a JSON file
with open(f'{e_id}.json', 'w') as new_file:
    json.dump(dataSet, new_file)
