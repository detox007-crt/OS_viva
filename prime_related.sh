#!/bin/bash

echo "Enter a number:"
read num

# 0 and 1 are not prime numbers
if [ $num -le 1 ]; then
    echo "$num is not a prime number"
    exit 0
fi

# Assume number is prime
is_prime=1

# Loop from 2 to num-1
for (( i=2; i<=$num/2; i++ ))
do
    if [ $((num % i)) -eq 0 ]; then
        is_prime=0
        break
    fi
done

if [ $is_prime -eq 1 ]; then
    echo "$num is a prime number"
else
    echo "$num is not a prime number"
fi
