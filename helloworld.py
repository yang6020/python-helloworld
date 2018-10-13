#!/usr/local/bin/python3

# pylint: disable=E0401
import requests

response = requests.get('https://httpbin.org/ip')
# single line comment
""" 
multi 
line
comment 
"""

isTrue = True


def printme(varIsTrue):
    if varIsTrue:
        print('true')
    else:
        print('false')


longname = \
    "hello" + \
    "long" + \
    "world"

num1 = 1
num3 = num1

num4 = num3 + num1


print('Your IP is {0}'.format(response.json()['origin']))
print(num4)
num1 = 2
print(num4)
print(longname)
printme(isTrue)
isTrue = False
printme(isTrue)
