#!/bin/bash
# only status
curl -so /dev/null -w "%{http_code}" "$1"
