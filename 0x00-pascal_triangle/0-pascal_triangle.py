#!/usr/bin/python3
"""
pascal_triangle
"""


def pascal_triangle(n):
    """returns the list of a number's pascal triangle"""

    result = []
    if n > 0:
        for i in range(1, n + 1):
            each = []
            first = 1
            for j in range(1, i + 1):
                each.append(first)
                first = first * (i - j) // j
            result.append(each)
    return result