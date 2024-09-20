#!/usr/bin/python3
"""Interview Mockups - MakeChange"""


import heapq


def makeChange(coins, total):
    """
        Given a pile of coins of different values,
        determine the fewest number of coins needed
        to meet a given amount total.
    """
    if total <= 0:
        return 0

    # Initialize the dp array with a large value (total + 1)
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] <= total else -1
