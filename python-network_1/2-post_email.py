#!/usr/bin/python3
"""Python script that takes in a URL and EMAIL then
sends a POST to the URL and displays the body of the response
"""


import requests
import sys

url_take = sys.argv
if len(url_take) < 3:
        print("Please, Provide url address and the email address next to cmd")
        exit(1)
url = url_take[1]
email = url_take[2]

if __name__ == "__main__":
    data = {"Your email address is": email}
    response = requests.post(url, data=data)
    print(response.text)