
# Strassen's Matrix Multiplication

## Aim
To multiply two matrices using Strassen's Divide and Conquer algorithm.

## Algorithm
1. Divide both matrices into four submatrices.
2. Calculate seven intermediate products.
3. Use these products to calculate four result submatrices.
4. Combine the submatrices to get the final product.
5. Pad matrices with zeros when needed to make their dimensions a power of two.

## Pseudocode
STRASSEN(A, B):
    IF size(A) == 1:
        RETURN A * B

    DIVIDE A AND B INTO FOUR PARTS
    CALCULATE M1, M2, M3, M4, M5, M6, M7
    CALCULATE C11, C12, C21, C22
    COMBINE FOUR RESULT PARTS
    RETURN C

## Complexity Analysis
- Time Complexity: O(n^log2(7)) ≈ O(n^2.807)
- Auxiliary Space: O(n^2) for matrix storage, excluding recursion overhead.

## Sample Output
[30, 24, 18]
[84, 69, 54]
[138, 114, 90]

## Learning Outcomes
- Understood Strassen's matrix multiplication.
- Learned matrix division and combination.
- Understood how reducing recursive multiplications improves complexity.
