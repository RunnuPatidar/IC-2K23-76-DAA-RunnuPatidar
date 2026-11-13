
# 0/1 Knapsack using Dynamic Programming

## Aim
To find the maximum value of items that can be placed in a knapsack without exceeding its capacity.

## Algorithm
1. Create a DP table of size (n+1) x (W+1).
2. Initialize the first row and column with zero.
3. Consider each item and each capacity.
4. If the item fits, choose the maximum of including or excluding it.
5. Otherwise, exclude the item.
6. Trace the table to find selected items.

## Pseudocode
FOR i = 1 TO n:
    FOR w = 0 TO W:
        IF weight[i] <= w:
            DP[i][w] = MAX(
                value[i] + DP[i-1][w-weight[i]],
                DP[i-1][w]
            )
        ELSE:
            DP[i][w] = DP[i-1][w]

RETURN DP[n][W]

## Complexity Analysis
- Time Complexity: O(nW)
- Space Complexity: O(nW)

## Sample Output
Maximum Value: 7

## Learning Outcomes
- Understood the 0/1 Knapsack problem.
- Learned tabulation.
- Understood optimal substructure and overlapping subproblems.
