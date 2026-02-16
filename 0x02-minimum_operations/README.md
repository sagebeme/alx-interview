0x02. Minimum operations
========================

This project computes the **minimum number of operations** to get from 1 to `n` when the only operations are "copy all" and "paste". You practice dynamic programming or greedy reasoning.

Tasks
-----

### 0. Minimum operations

mandatory

Implement a function `minOperations(n)` that returns the minimum number of copy-all and paste operations needed to have exactly n characters in a file (starting from 1). Run: `python3 0-main.py` or import and call `minOperations(n)`.

**Repo:**

-   GitHub repository: `alx-interview`
-   Directory: `0x02-minimum_operations`
-   File: (main solution file)

---

**How to do the exercises yourself**

1. Relate the problem to the sum of prime factors of `n` (or build the sequence of operations).
2. Handle edge case `n <= 1` (return 0).
