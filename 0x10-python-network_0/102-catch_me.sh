#!/bin/bash
# cause a server to respond with a custom text ("You got me!")
curl -sLX PUT -H "Origin:School" -d "user_id=98" "0.0.0.0:5000/catch_me"
