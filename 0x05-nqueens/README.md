0x05. N-queens
==============

This project solves the **N-queens** problem: place N queens on an N×N chessboard so that no two attack each other. You print every solution (or the first). You practice backtracking.

Tasks
-----

### 0. N-queens

mandatory

Read N from command line (e.g. `python3 0-nqueens.py 4`), then print every valid placement of N queens (one per line, e.g. as list of [row, col] or coordinates). Run: `python3 0-nqueens.py N`.

**Repo:**

-   GitHub repository: `alx-interview`
-   Directory: `0x05-nqueens`
-   File: `0-nqueens.py`

---

**How to do the exercises yourself**

1. Use backtracking: place a queen in the next row, check columns and diagonals, recurse or backtrack.
2. Print each solution in the required format.
