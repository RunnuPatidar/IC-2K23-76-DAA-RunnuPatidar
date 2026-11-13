
# Fractional Knapsack using Greedy Method

## Aim
To solve the Fractional Knapsack problem using the Greedy approach.

## Algorithm
1. Calculate the value-to-weight ratio of each item.
2. Sort items in descending order of this ratio.
3. Select the item with the highest ratio.
4. If the complete item fits, add it to the knapsack.
5. Otherwise, take the fraction that fits.
6. Continue until the capacity becomes zero.

## Pseudocode
SORT items by value/weight ratio in descending order
TOTAL = 0

FOR each item:
    IF item weight <= remaining capacity:
        TAKE complete item
    ELSE:
        TAKE required fraction

    UPDATE TOTAL VALUE

RETURN TOTAL

## Complexity Analysis
- Sorting: O(n log n)
- Selection: O(n)
- Overall Time Complexity: O(n log n)
- Auxiliary Space: O(n)

## Sample Input
Capacity = 50

Items:
(Weight=10, Value=60)
(Weight=20, Value=100)
(Weight=30, Value=120)

## Sample Output
Maximum Value: 240.0

## Learning Outcomes
- Understood the Greedy strategy.
- Learned value-to-weight ratio calculation.
- Learned how fractional selection works.
