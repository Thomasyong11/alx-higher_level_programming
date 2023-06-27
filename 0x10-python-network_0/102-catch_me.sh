#!/bin/bash
# Make the request and capture the response
response=$(curl -s 0.0.0.0:5000/catch_me -XPUT -H "Origin:You got me!")

# Store the message in a variable
message=$(grep -o "You got me!" <<< "$response")

# Print the message by redirecting it to stdout
printf "%s\n" "$message"
