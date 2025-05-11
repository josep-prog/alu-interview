#!/usr/bin/python3

"""
This function computes the minimum number of operations needed to get n 'H'
characters in a text file, starting from one 'H'. It does so by breaking n
into its prime factors. Each prime factor represents a sequence of operations,
and the sum of all these factors gives the fewest operations required.
"""


def minOperations(n):
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
