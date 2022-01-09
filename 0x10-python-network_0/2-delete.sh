#!/bin/bash
# sends a DELETE request to the URL passed as the first argument and displays the body
curl -sL -DELETE "$1"
