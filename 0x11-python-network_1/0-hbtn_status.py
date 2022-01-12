#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    import urllib.request

    req = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(req) as response:
        html = response.read()

    print(f"""Body response:
        - type: {type(html)}
        - content: {html}
        - utf8 content: {html.decode('utf8')}""")
