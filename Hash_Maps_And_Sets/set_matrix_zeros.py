""" Leetcode problem 73: Set Matrix Zeroes https://leetcode.com/problems/set-matrix-zeroes/
1) Set up variables, check if empty matrix
2) Pass 1: Traverse through the matrix to identify the rows and columns 
containing zeros and store their indexes in hash sets
3) Pass 2: Traverse again and set any cell in the matrix to zero 
if its row index is in 'zero_rows' hash set or its column index is in 'zero_cols' hash set
Time: O(n^2)
Space: O(n^2)
"""

def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    if not matrix or not matrix[0]:
        return
    m, n = len(matrix), len(matrix[0])
    zero_rows, zero_cols = set(), set()
    for r in range(m):
        for c in range(n):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)
    for r in range(m):
        for c in range(n):
            if r in zero_rows or c in zero_cols:
                matrix[r][c] = 0

"""
“Your solution uses O(m + n) space for sets. Can we do it with constant space?”

Yes. Instead of using extra sets, we can use the first row and first column of the matrix as markers.
For each cell that is zero, we set its row’s first element and column’s first element to zero.
Later, we iterate again to zero out all cells based on these markers.
Finally, we check if the first row or first column themselves need to be zeroed and handle them separately.
This way, we don’t allocate any extra memory proportional to m or n—just two booleans 
for the first row and column—so the extra space is O(1).”
----------------------
“Can you do it faster than O(m × n)?”
Every element could potentially be affected by zeros, so you must inspect all m × n elements at least once.
Therefore, O(m × n) is most optimal.
"""