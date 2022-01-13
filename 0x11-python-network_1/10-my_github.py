#!/usr/bin/python3
"""Write a Python script that takes 2 arguments
in order to solve this challenge
"""
from sys import argv
import requests


if __name__ == '__main__':

    url = "https://api.github.com/user"
    r = requests.get(url, auth=(argv[1], argv[2]))
    res = r.json()
    print(res.get('id'))
