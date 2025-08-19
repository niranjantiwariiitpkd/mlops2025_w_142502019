#!/bin/bash

echo "Enter a number:"
read n

sum=0

for (( i=1; i<=n; i++ ))
do
  sum=$((sum + i))
done

echo "Sum of numbers from 1 to $n is: $sum"



# Calculate factorial of n
factorial=1
for (( i=1; i<=n; i++ ))
do
  factorial=$((factorial * i))
done

echo "Factorial of $n is: $factorial"
