#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""
from sys import argv
import urllib.request
import urllib.parse


if __name__ == "__main__":

    value = {'email': argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        html = response.read()

    print(html)
