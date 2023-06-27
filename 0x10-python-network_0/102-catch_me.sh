#!/bin/bash
# Script that makes a request to causes an specific response
response=$(curl -sL 0.0.0.0:5000/catch_me -X PUT -H "Origin:You got me!")

# Store the message in a variable
message=$(grep -o "You got me!" <<< "$response")

# Print the message by redirecting it to stdout
printf "%s\n" "$message"
