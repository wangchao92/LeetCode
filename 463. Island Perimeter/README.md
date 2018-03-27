# Solution

Scan each cell, if the cell is 0 then continue, if not, check its surrounding 4 cells (up, down, left, right) if it is 0 then perimeter plus 1. Surroundings outside the boundary are considered as 0.

# Complexity

O(m*n) m is height and n is width
