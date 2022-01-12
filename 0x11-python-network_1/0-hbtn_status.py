#!/usr/bin/python3
import urllib.request

req = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    html = response.read()

print(f"""Body response:
    - type: {type(html)}
    - content: {html}
    - utf8 content: {html.decode('utf8')}""")
