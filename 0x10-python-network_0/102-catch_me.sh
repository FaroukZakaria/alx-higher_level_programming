#!/bin/bash
# cause a server to respond with a custom text ("You got me!")
curl -sLX PUT -d "user_id=98" -H "Origin: HolbertonSchool" \
    --data-raw "You got me!" "0.0.0.0:5000/catch_me" -w "\n"
