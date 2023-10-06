#!/usr/bin/python3

""" Python script to export data in the JSON format.

The script fetches data from a REST API about an employee's TODO
items and completion status.
It retrieves the employee details and each TODO task, then saves
the aggregated data to a JSON file. for all employee iterativelly

Usage:
  python 3-dictionary_of_list_of_dictionaries.py

Args:
    No args

Example:
  To export data for employee ID:
  python3 3-dictionary_of_list_of_dictionaries.py

"""

import json
import requests

if __name__ == "__main__":
    dataSet = {}
    id = 1
    while True:
        api_url = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
        employee_detail = f'https://jsonplaceholder.typicode.com/users/{id}'

        # Fetch specific employee details
        res = requests.get(employee_detail)
        eData = res.json()
        username = eData.get('username', '')

        # Initialize an empty list to store task data
        tasksList = []

        # Fetch TODO items for the employee with the given ID
        response = requests.get(api_url)
        data = response.json()

        if not data:
            break

        # Create a list of dictionaries for each task
        for item in data:
            user_id = int(item.get('userId', ''))
            if (id == user_id):
                task = item.get('title', '')
                status = item.get('completed', False)
                tasksList.append({'username': username, 'task': task,
                                'completed': status})    
        dataSet[id] = tasksList
        id+=1

        

    # Write the data to a JSON file
    with open('todo_all_employees.json', 'w') as new_file:
        json.dump(dataSet, new_file)