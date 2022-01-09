#!/bin/bash
# takes in a URL as an argument, sends a GET request to the URL, and displays the body
curl -sH "X-School-User-Id:98" GET "$1"
