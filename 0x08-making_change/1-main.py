#!/usr/bin/python3
"""
Main file for testing
"""


import sys


makeChange = __import__('0-making_change').makeChange

coins = []
for i in range(1, 1000, 7):
    coins.append(i)
print(makeChange(coins, 16576))