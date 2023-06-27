#!/bin/bash
curl -s 0.0.0.0:5000/catch_me -XPUT -d "user_id=98" -L -o response.txt

# Print the message from the response file
grep -o "You got me!" response.txt
