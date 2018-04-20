# Solution

Valid numbers are 0, 1, 2, 5, 6, 8, 9 and others are invalid. Good numbers are 2, 5, 6, 9. We maintain two flag variables, one for validity and the other one for "good". In order to verify if a number is good, at least one digit needs to be good while others need to be valid. So we just check each digit and update the flag variables.

# Complexity

O(n*k) k is the number of digits of N.
