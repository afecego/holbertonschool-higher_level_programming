#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -si -X OPTIONS -L "$1" | grep -i Allow: | cut -b 8-
