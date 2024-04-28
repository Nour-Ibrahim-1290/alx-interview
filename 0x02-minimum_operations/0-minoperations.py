#!/usr/bin/python3
""" Interview Practices"""


def minOperations(n):
    """
        Your text editor can execute only two operations
        in this file: Copy All and Paste.
    """
    if n <= 1:
        return 0
    num_operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            num_operations += divisor
            n = n // divisor
        divisor += 1
    return num_operations
