#!/usr/bin/python3

""" Function to find perimiter of an island """


def island_perimeter(grid):
    """Getting the perimeter of island

    Args:
        grid (_type_): the grid containing
        the island
    """
    def dfs(r, c):
        """
        Purpose: Function that calculates horizontal and vertical connections.
        """
        # Check and explore the four neighboring cells
        if r < 0 or r >= nr or c < 0 or c >= nc or grid[r][c] == 0:
            return 1  # If out of bounds or water, count as perimeter

        if grid[r][c] == -1:
            return 0  # If already visited, no additional perimeter

        grid[r][c] = -1  # Mark cell as visited

        perimeter = (
            dfs(r - 1, c)
            + dfs(r + 1, c)
            + dfs(r, c - 1)
            + dfs(r, c + 1)
        )

        return perimeter

    nr = len(grid)
    if nr == 0:
        return 0
    nc = len(grid[0])
    per_island = 0
    for r in range(nr):
        for c in range(nc):
            if grid[r][c] == 1:
                per_island += dfs(r, c)
    return per_island

