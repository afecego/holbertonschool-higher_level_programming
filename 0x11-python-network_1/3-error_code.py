#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
and displays the body of the response
"""
import urllib.request
import urllib.error
from sys import argv


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            print(html)
    except urllib.error.HTTPError as error:
        print("Error code: {:}".format(error.code))
