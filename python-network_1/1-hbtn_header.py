#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header"""


import requests
import sys

url_take = sys.argv
if len(url_take) < 2:
        print("Please, Provide url address next to cmd")
        exit(1)

if __name__ == "__main__":
    if len(url_take) == 2:
        response = requests.get(url_take[1])

        if response.status_code == 200:
                print(response.headers.get('X-Request-Id'))
