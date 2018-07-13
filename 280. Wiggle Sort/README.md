# Solution
Assume that numbers of index from 0 to i are sorted according to the requirements. num[i] and num[i + 1] are not sorted.
*** Case 1: if i is even, then num[i - 1] <= num[i] < num[i + 1]
*** Case 2: if i is odd, then num[i + 1] >= num[i] > num[i + 1]
In both cases, after we swap num[i] and num[i + 1], 0 to i + 1 will be sorted and we can move on to i + 1 and i + 2.

# Complexity
O(n)
