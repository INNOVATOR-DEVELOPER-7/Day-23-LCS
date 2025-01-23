# Day-23-LCS
Here's Python Program for LCS(Longest Common Subsequence). Day 23 of Day 365.

Step-by-Step Illustration:

1. Sequences:
   - Sequence 1: ABCD
   - Sequence 2: ACBD

2. Matrix Setup:
   ```
      0  A  C  B  D
   0  0  0  0  0  0
   A  0  -  -  -  -
   B  0  -  -  -  -
   C  0  -  -  -  -
   D  0  -  -  -  -
   ```

3. Filling the Matrix:
   - Start comparing characters.
   - If they match, add 1 to the diagonal cell.
   - If they don't match, take the maximum value from the cell above or to the left.

   Here’s how it looks as we fill it:

   ```
      0  A  C  B  D
   0  0  0  0  0  0
   A  0  1  1  1  1
   B  0  1  1  2  2
   C  0  1  2  2  2
   D  0  1  2  2  3
   ```

4. Tracing Back to Find the LCS:
   - Starting from the bottom-right cell, trace back to reconstruct the LCS.
   - If characters match, they are part of the LCS.
   - Move diagonally up to the left.
   - If they don't match, move in the direction of the higher value (either up or left).

   Tracing back, we get:
   - 'D' (bottom-right cell)
   - 'C' (diagonal up-left from 'D')
   - 'A' (diagonal up-left from 'C')

   So, the LCS is "ACD".

Summary:
- The matrix helps us determine the length and the actual subsequence.
- The filled matrix shows the LCS length in the bottom-right cell.
- Tracing back reveals the LCS itself.
