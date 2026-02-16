0x0A. Prime game
================

This project implements the **prime game**: two players take turns choosing a prime number and removing it and its multiples from the set {1, 2, ..., n}. The player who cannot move loses. You determine the winner (Maria or Ben) for a given `n`.

Tasks
-----

### 0. Prime game

mandatory

Implement a function `isWinner(x, nums)` where x is the number of rounds and nums is a list of n values. For each round, the game is played with set {1..n}; return the name of the player who won the most rounds ("Maria" or "Ben"), or None if tied. Run: `python3 0-main.py` or import and call.

**Repo:**

-   GitHub repository: `alx-interview`
-   Directory: `0x0A-primegame`
-   File: (main solution file)

---

**How to do the exercises yourself**

1. For each n, compute whether the first player (Maria) can force a win (e.g. by recursion or precomputation).
2. Count wins per player across rounds and return the winner.
