#!/bin/bash

# Send a POST request to the specified URL with a custom header
curl -s -X POST -H "Origin: HolbertonSchool" -d "user_id=98" "http://0.0.0.0:5000/catch_me"
