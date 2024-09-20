#!/usr/bin/python3
"""Interview Mockups - MakeChange"""


import heapq
import numpy as np


def makeChange(coins, total):
    """
        Given a pile of coins of different values,
        determine the fewest number of coins needed
        to meet a given amount total.
    """
    # if total <= 0:
    #     return 0

    # # Sort coins in descending order
    # coins.sort(reverse=True)

    # # Priority queue to keep track of the minimum number of coins
    # pq = [(0, 0)]  # (number of coins, current total)
    # visited = set()

    # while pq:
    #     num_coins, curr_total = heapq.heappop(pq)

    #     if curr_total == total:
    #         return num_coins

    #     if curr_total > total or curr_total in visited:
    #         continue

    #     visited.add(curr_total)

    #     for coin in coins:
    #         heapq.heappush(pq, (num_coins + 1, curr_total + coin))

    # return -1
    if total <= 0:
        return 0

    # Initialize the dp array with a large value (total + 1)
    dp = np.full(total + 1, total + 1, dtype=int)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return int(dp[total]) if dp[total] <= total else -1
