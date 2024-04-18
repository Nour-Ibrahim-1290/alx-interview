#!/usr/bin/python3
"""
0. Lock Boxes
"""


def canUnlockAll(boxes):
    """
    Returns a boolean that determines if all the boxes can be opened.
    """
    keys = set(boxes[0])
    unlocked = set([0])

    while keys:
        new_keys = set()
        for key in keys:
            if key not in unlocked:
                unlocked.add(key)
                new_keys.update(boxes[key])
        if not new_keys:
            break
        keys = new_keys

    return len(unlocked) == len(boxes)
