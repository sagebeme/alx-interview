0x00. Pascal's triangle
=======================

This project implements **Pascal's triangle** in Python: given `n`, return a list of lists representing the first `n` rows of Pascal's triangle. You practice list building and the mathematical relationship between rows.

Tasks
-----

### 0. Pascal's triangle

mandatory

Implement a function `pascal_triangle(n)` that returns a list of lists of integers representing the first n rows of Pascal's triangle. Each row is a list of integers; each element is the sum of the two elements above it (or 1 on the edges). Run: `python3 0-main.py` or import and call `pascal_triangle(5)` to see the result.

**Repo:**

-   GitHub repository: `alx-interview`
-   Directory: `0x00-pascal_triangle`
-   File: `0-pascal_triangle.py`

---

**How to do the exercises yourself**

1. Implement the function that builds each row from the previous row.
2. Return a list of lists; ensure the first row is `[1]` and the second is `[1, 1]`.
3. Run the provided main or tests to verify output.
