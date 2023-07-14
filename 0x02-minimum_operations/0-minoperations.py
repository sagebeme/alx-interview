#!/usr/bin/python3

"""return an integer"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The fewest number of operations needed.

    """

    # If n is less than 2, it is impossible to achieve
    if n < 2:
        return 0

    # Initialize the number of operations and the clipboard with 1 H character
    num_operations = 0
    clipboard = 1

    # Start with 2 H characters already in the file
    file_content = 2

    while file_content < n:
        if n % file_content == 0:
            # If the current file content is a factor of n, we can Copy All and Paste multiple times
            num_paste_operations = n // file_content - 1
            num_operations += num_paste_operations + 1
            clipboard = file_content
        else:
            # If the current file content is not a factor of n, we can only Paste
            num_operations += 1
            file_content += clipboard

    return num_operations 
