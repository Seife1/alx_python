#!/usr/bin/python3
"""Project - Python Network"""


from urllib import request

with request.urlopen('https://alu-intranet.hbtn.io/status') as response:

    try:
        content = response.read().decode('utf-8')
        print('Body response:')
        print('\t- type: ', type(content))
        print("\t- content: ", content,)
    except Exception as e:
        print(e)