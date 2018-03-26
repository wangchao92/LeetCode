# Solution

Maintain a list and a variable "sum". When we move the window, we need to remove number from the beginning of the list and append new number to the end.
At the same time, we subtract removed number from sum and add the new number to it. This can avoid recalculating sum every time.

# Complexity
O(1)
