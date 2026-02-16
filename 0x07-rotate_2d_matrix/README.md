0x07. Rotate 2D matrix
======================

This project **rotates an n×n matrix 90 degrees clockwise** in place. You practice matrix indexing and in-place updates.

Tasks
-----

### 0. Rotate 2D matrix

mandatory

Implement a function `rotate_2d_matrix(matrix)` that rotates the given n×n matrix 90 degrees clockwise without allocating a new matrix. Run: `python3 0-main.py` or import and call with a 2D list.

**Repo:**

-   GitHub repository: `alx-interview`
-   Directory: `0x07-rotate_2d_matrix`
-   File: (main solution file)

---

**How to do the exercises yourself**

1. Rotate layer by layer (outer to inner); for each element, swap four positions in a cycle.
2. Ensure in-place: no extra 2D matrix, only a few temp variables if needed.
