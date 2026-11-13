# Sum of Subsets

## Aim
To find subsets of a given set whose sum equals a target value
using backtracking.

## Theory
The Sum of Subsets problem finds combinations of elements
whose total is equal to a specified target.

Backtracking explores possible combinations by including
or excluding each element.

## Algorithm
1. Initialize the given set and target sum.
2. Start from the first element.
3. Include the current element and update the sum.
4. Check whether the target sum is reached.
5. If the sum exceeds the target, backtrack.
6. Exclude the current element and explore the remaining elements.
7. Display all valid subsets.

## Time Complexity
O(2^n), where n is the number of elements.

## Space Complexity
O(n), excluding the output.

## Sample Output
Subset found: [3, 4, 5]
Subset found: [5, 7]

## Learning Outcome
Learned to find valid subsets using recursive backtracking.