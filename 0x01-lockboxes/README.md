0x01. Lockboxes
===============

This project solves the **lockboxes** problem: you have `n` boxes (list of lists); each box may contain keys to other boxes. Determine whether all boxes can be opened (starting from box 0). You practice graph traversal (BFS or DFS).

Tasks
-----

### 0. Can unlock all

mandatory

Implement a function `canUnlockAll(boxes)` that returns True if all boxes can be opened, False otherwise. You start with box 0 and use keys inside boxes to open others. Run: `python3 0-main.py` or import and call with a list of boxes.

**Repo:**

-   GitHub repository: `alx-interview`
-   Directory: `0x01-lockboxes`
-   File: `0-lockboxes.py`

---

**How to do the exercises yourself**

1. Treat boxes as nodes and keys as edges; traverse from box 0.
2. Track which boxes are opened; return True when all are reachable.
