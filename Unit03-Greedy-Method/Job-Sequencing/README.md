
# Job Sequencing with Deadlines

## Aim
To schedule jobs with deadlines to maximize total profit using the Greedy Method.

## Algorithm
1. Sort jobs in descending order of profit.
2. Find the maximum deadline.
3. Create available time slots.
4. Select jobs in descending order of profit.
5. Place each job in the latest available slot before its deadline.
6. Calculate the total profit.

## Pseudocode
SORT jobs by decreasing profit
CREATE empty slots

FOR each job:
    FOR slot from deadline down to 1:
        IF slot is empty:
            ASSIGN job to slot
            ADD profit
            BREAK

RETURN schedule and total profit

## Complexity Analysis
- Time Complexity: O(n log n + nD), where D is the maximum deadline.
- Auxiliary Space: O(D)

## Sample Output
Selected Jobs: J3, J1, J5
Maximum Profit: 142

## Learning Outcomes
- Understood job scheduling.
- Learned deadline-based selection.
- Applied Greedy strategy to maximize profit.
