# 0/1 Knapsack using Branch and Bound

## Aim
To solve the 0/1 Knapsack problem using Branch and Bound.

## Theory
Branch and Bound is an optimization technique that divides
a problem into smaller subproblems.

It calculates an upper bound to eliminate branches
that cannot produce a better solution.

## Algorithm
1. Define item weights, profits and capacity.
2. Sort items by profit-to-weight ratio.
3. Calculate the upper bound for each node.
4. Explore the branch that includes the current item.
5. Explore the branch that excludes the current item.
6. Prune branches whose upper bound cannot improve the result.
7. Display the maximum profit and selected items.

## Time Complexity
O(2^n) in the worst case.

## Space Complexity
O(n), excluding the input and sorting storage.

## Sample Output
Maximum Profit: 220
Total Weight: 50

## Learning Outcome
Learned how Branch and Bound reduces unnecessary
search while solving an optimization problem.