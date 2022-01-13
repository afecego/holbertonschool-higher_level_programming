#!/usr/bin/python3
"""script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user
"""
from sys import argv
import requests


if __name__ == "__main__":

    URL = "http://2ad4c0d5a99f.2c554f59.hbtn-cod.io:5000/search_user"

    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    dic = {'q': q}
    try:
        req = requests.post(URL, dic).json()
        if len(req) == 0 or not req.get('id') or not req.get('name'):
            print("No result")
        else:
            print("[{}] {}".format(req.get('id'), req.get('name')))
    except ValueError:
        print("Not a valid JSON")
