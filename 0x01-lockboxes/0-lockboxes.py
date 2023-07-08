#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    creates a set to keep track of all boxes visited
    """
    visited = set()
    visited.add(0)

    stack = [0] # Use a stack to perform depth-first search
    
    # perform DFS
    while stack:
        box = stack.pop()

        # check if you have a key to open other boxes
        for key in boxes[box]:
            if not key in visited:
                visited.add(key)
                stack.append(key)
    # check if all boxes have been visited
    return len(visited) == len(boxes)