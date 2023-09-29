#!/bin/bash
# Curl to get body size
curl -sw '%{size_download}\n' -o /dev/null $1
