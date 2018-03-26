# Solution

As Up and Down are opposite, Left and Right are opposite, we can maintain two stacks. One for U and D, and other one for L and R.
When we read a U/D, check if the stack is empty. If it is empty, push into stack. If it's not, check whether the read character is same as the top of stack.
If not, pop, if yes, push.
Same operations apply to L/R.

# Complexity

O(n)
