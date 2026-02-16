0x08. Making change
===================

This project solves the **making change** problem: given a list of coin denominations and a total amount, find the **minimum number of coins** needed to make that amount (or 0 if impossible). You practice greedy or dynamic programming.

Tasks
-----

### 0. Making change

mandatory

Implement a function `makeChange(coins, total)` that returns the minimum number of coins needed to make total from coins, or -1 if impossible. Run: `python3 0-main.py` or import and call with a list of coins and a total.

**Repo:**

-   GitHub repository: `alx-interview`
-   Directory: `0x08-making_change`
-   File: (main solution file)

---

**How to do the exercises yourself**

1. Use a greedy approach (largest coins first) if the coin set allows; otherwise DP.
2. Return -1 when total cannot be formed.
