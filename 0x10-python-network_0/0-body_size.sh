#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body
curl -sI "$1":5000 | grep -i content-length | awk '{print $2}'
