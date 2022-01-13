#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id
"""
from sys import argv
import requests


if __name__ == "__main__":

    r = requests.get(argv[1])
    id = r.headers.get('X-Request-Id')
    print(id)
