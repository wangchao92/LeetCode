# Solution

As we do not need to output the location of added letter (we actually do not know as the string has been shuffled), we can just save s into a dictionary (letter as key, frequency as value).
Then we read the second string t and lookup letter in dictionary. Deduct frequency, when we found the letter in t has 0 requency in s or it is not a key, it is the letter added.

# Complexity

O(n)
