#!/bin/bash
# Get the size of the response header from a URL.
curl -s "$1" | wc -c

