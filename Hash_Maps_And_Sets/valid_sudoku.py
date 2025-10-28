from typing import List

""" Leetcode Problem 36: Valid Sudoku https://leetcode.com/problems/valid-sudoku/
1) Create hash sets for each row, column, and subgrid
2) Check if num has already been seen in this row, column, or subgrid
3) If we pass step 2's checks, then mark this num as seen - add to hash sets
Use list comprehension - convenient and fast
    _ is just a throwaway variable name 
Time: O(n^2⋅1) = O(n^2)
    constant time hash set operations for each cell in the board
Space: O(n^2) + O(n^2) + O(n^2) = O(n^2)
    n hash sets capable of growing to a size of n for each
"""


def isValidSudoku(self, board: List[List[str]]) -> bool:
    if not board or not board[0]:
        return False
    row_sets = [set() for _ in range(9)]
    col_sets = [set() for _ in range(9)]
    subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]
    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == ".":
                continue
            if num in row_sets[r]:
                return False
            if num in col_sets[c]:
                return False
            if num in subgrid_sets[r // 3][c // 3]:
                return False
            row_sets[r].add(num)
            col_sets[c].add(num)
            subgrid_sets[r // 3][c // 3].add(num)
    return True


"""
What if it wasn't a 9x9 board, but an nxn board?
I would adjust like so: 
n = len(board)
subgrid_size = int(sqrt(n))
and replace the corresponding numbers with those variables
------------------------
"What about invalid input including if a number is out of the range of 1 to 9?"
I would add a check like so: 
if num != '.' and (not num.isdigit() or not (1 <= int(num) <= n)):
    return False
-------------------------
“Your solution uses sets for rows, columns, and subgrids. Can we reduce space to constant O(1)?”
Yes, using bit masks. 
1. Represent rows, columns, and subgrids as 9-bit integers. Bits are indexed 0–8 (bit 0 = number 1, bit 1 = number 2, …, bit 8 = number 9).
If seen, that bit is 1
subgrid_index = (r//3) * 3 + c//3
    - Use 2D array flattening formula: index = row_index * num_cols + col_index
(r, c) range	subgrid_index
(0–2, 0–2)	        0
(0–2, 3–5)	        1
(0–2, 6–8)	        2
(3–5, 0–2)	        3
    etc.

2. Check for dupes with bitwise AND & using the mask - rows[r] & mask isolates just the bit for num.
mask = 1 << (num - 1)
    - Because
        3	1 << 2	000000100
        9	1 << 8	100000000
            etc.

if rows[r] & mask:
    return False  
        # bitwise AND (&) operation:
        # If both numbers have the same bit set → result is nonzero (duplicate).
        # If not → result is zero (no duplicate yet).

3. If not a dupe, mark as aseen using bitwise OR | - OR operation sets the corresponding bit to 1 without changing other bits.
rows[r] |= mask
cols[c] |= mask
subgrids[subgrid_index] |= mask

Below is the bitmasking solution
"""


def isValidSudokuOptimized(board: List[List[str]]) -> bool:
    if not board or not board[0]:
        return False
    rows = [0] * 9
    cols = [0] * 9
    subgrids = [0] * 9

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            num = int(board[r][c])
            mask = 1 << (num - 1)
            subgrid_index = (r // 3) * 3 + (c // 3)

            if rows[r] & mask or cols[c] & mask or subgrids[subgrid_index] & mask:
                return False

            rows[r] |= mask
            cols[c] |= mask
            subgrids[subgrid_index] |= mask

    return True
