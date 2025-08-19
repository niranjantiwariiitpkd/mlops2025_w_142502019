#!/bin/bash

echo "Enter a number:"
read n

# Calculate sum
sum=0
for (( i=1; i<=n; i++ ))
do
  sum=$((sum + i))
done
echo "Sum of numbers from 1 to $n is: $sum"

# Factorial of sum
factorial=1
for (( i=1; i<=sum; i++ ))
do
  factorial=$((factorial * i))
done
echo "Factorial of $sum is: $factorial"

# Numerical difference
difference=$((factorial - sum))

# Write both code diff and numeric difference into output.txt
{
  echo "===== CODE DIFFERENCE ====="
  diff add.sh add_rev1.sh
  echo
  echo "===== NUMERICAL DIFFERENCE ====="
  echo "For n=$n:"
  echo "Sum = $sum"
  echo "Factorial(sum) = $factorial"
  echo "Difference = $difference"
} > output.txt
