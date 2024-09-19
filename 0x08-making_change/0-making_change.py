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

    # Sort coins in descending order
    coins.sort(reverse=True)

    # Priority queue to keep track of the minimum number of coins
    pq = [(0, 0)]  # (number of coins, current total)
    visited = set()

    while pq:
        num_coins, curr_total = heapq.heappop(pq)

        if curr_total == total:
            return num_coins

        if curr_total > total or curr_total in visited:
            continue

        visited.add(curr_total)

        for coin in coins:
            heapq.heappush(pq, (num_coins + 1, curr_total + coin))

    return -1
