#!/usr/bin/python3
"""
    A Python script that, using REST API, for a given employee ID,
    Returns information about his/her TODO list progress then
    Extend your Python script to export data in the CSV format.

    Usage:
    python 2-export_to_JSON.py <employee_id>

    Args:
        e_id (int): The ID of the employee to fetch data for.

    Example:
        To fetch data for employee ID 1:
        python3 2-export_to_JSON.py 1
"""

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
