
# Experiment 4: Complexity Analysis

## Aim
To analyze the best, average and worst-case
time complexity of Linear Search.

## Problem Statement
Analyze the number of comparisons required
by Linear Search for different input cases.

## Algorithm
1. Initialize an array.
2. Select a target element.
3. Compare the target with each array element.
4. Count the comparisons.
5. Return the index if found.
6. Display the number of comparisons.

## Pseudocode
START
comparisons = 0
FOR each element in array
    comparisons = comparisons + 1
    IF element == target
        RETURN index
RETURN -1
STOP

## Complexity Analysis

| Case | Time Complexity |
|---|---|
| Best | O(1) |
| Average | O(n) |
| Worst | O(n) |

Space Complexity: O(1)

## Sample Results
Best Case: 1 comparison
Average Case: 4 comparisons
Worst Case: 7 comparisons

## Learning Outcomes
- Understood algorithm complexity.
- Learned best, average and worst cases.
- Analyzed the number of comparisons.
