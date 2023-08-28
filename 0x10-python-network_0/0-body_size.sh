#!/bin/bash
# Get the size of the response header from a URL.
curl -sI "$1" | grep 'Content-Length:' | cut -f2 -d' '

