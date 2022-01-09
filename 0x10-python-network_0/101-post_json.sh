#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument, and displays the body
curl -s -d @"$2" "Content-Type: application/json" -X POST "$1"
