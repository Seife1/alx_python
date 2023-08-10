#!/usr/bin/python3
"""Project - Python Network"""


import requests

if  __name__ == '__main__':
    response = requests.get('https://alu-intranet.hbtn.io/status')
    content = response.text
    
    print('Body response:')
    print('\t- type:', type(content))
    print("\t- content:", content,)