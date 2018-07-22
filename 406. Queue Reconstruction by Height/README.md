# Solution

We first sort the paris according to h (ascending) than k (descanding) if their h are same.
Then we start from the first person. As he is the shortest person, we know the number of people, and we know h. Thus, his position in the queue is confirmed. Than we move on to the next person. However, when we confirm their positions, we need to ignore the persons who have already been confirmed in the queue. i.e. h should be the hth pos in the queue excluding those who already in the queue.

# Complexity

O(n<sup>2</sup>)

# Improvement


