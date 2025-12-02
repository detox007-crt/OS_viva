#!/bin/bash

echo "Enter a string:"
read str

# Reverse the string
rev=$(echo "$str" | rev)

# Compare original with reversed
if [ "$str" = "$rev" ]; then
    echo "\"$str\" is a palindrome"
else
    echo "\"$str\" is not a palindrome"
fi
