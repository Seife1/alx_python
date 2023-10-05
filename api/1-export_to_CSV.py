#!/usr/bin/python3
"""
A Python script that, using REST API, for a given employee ID,
Returns information about his/her TODO list progress then
Extend your Python script to export data in the CSV format.
"""

import csv
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

for key in data:
    task_completed = key.get('completed')
    task_title = key.get('title')
    tasksList.append([e_id, username, task_completed, task_title])

# Write the data to a CSV file
with open(f'{e_id}.csv', 'w', newline='') as csv_file:
    fieldNames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    csv_writer.writerows(tasksList)
