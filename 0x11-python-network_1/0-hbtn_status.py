#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    import urllib.request

    req = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(req) as response:
        html = response.read()

    print("Body response:")
    print("\t- type: {:}".format(type(html)))
    print("\t- content: {:}".format(html))
    print("\t- utf8 content: {:}".format(html.decode('utf8')))
