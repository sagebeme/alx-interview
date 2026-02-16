0x09. Island perimeter
======================

This project computes the **perimeter of an island** in a 2D grid: cells with value 1 form the island; count the total length of edges that separate land from water (or grid boundary). You practice grid traversal.

Tasks
-----

### 0. Island perimeter

mandatory

Implement a function `island_perimeter(grid)` that returns the perimeter of the single island in the grid. Each land cell contributes 4 minus the number of adjacent land cells. Run: `python3 0-main.py` or import and call with a 2D list.

**Repo:**

-   GitHub repository: `alx-interview`
-   Directory: `0x09-island_perimeter`
-   File: (main solution file)

---

**How to do the exercises yourself**

1. Iterate over each cell; for each 1, add 4 and subtract the number of neighboring 1s.
2. Assume exactly one island and no water inside the island boundary.
