#!/usr/bin/python3
"""
Calculate how much rainwater is trapped
"""


def rain(walls):
    """
    Given a list of non-negative integers representing wall heights,
    calculate how much rainwater is trapped between the walls.

    Args:
        walls (list): List of non-negative integers

    Returns:
        int: Total amount of trapped water
    """
    if not walls or len(walls) < 3:
        return 0

    n = len(walls)
    total_water = 0

    # Create arrays to store highest wall to the left and right of each index
    left_max = [0] * n
    right_max = [0] * n

    # Fill left_max from left to right
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    # Fill right_max from right to left
    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    # Calculate trapped water at each index
    for i in range(1, n - 1):
        min_wall = min(left_max[i], right_max[i])
        if min_wall > walls[i]:
            total_water += min_wall - walls[i]

    return total_water
