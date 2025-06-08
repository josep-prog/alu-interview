#!/usr/bin/python3
"""
Generate Pascal's Triangle and print it
"""

def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for row_num in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for i in range(1, len(prev_row)):
            new_row.append(prev_row[i - 1] + prev_row[i])

        new_row.append(1)
        triangle.append(new_row)

    return triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join(str(x) for x in row)))

if __name__ == "__main__":
    # Change the number here to test different sizes
    print_triangle(pascal_triangle(5))
