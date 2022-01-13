#!/usr/bin/python3
"""script that takes in a URL and an email address,
sends a POST request to the passed URL
"""
from sys import argv
import requests


if __name__ == "__main__":
    payload = {'email': argv[2]}
    r = requests.post(argv[1], data=payload)
    print(r.text)
