#!/usr/bin/python3


import sys
import signal


def print_stats(status_codes, file_size):
    """
        Print the stats for a given list of status
    """
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    """
        Handle the signal
    """
    print_stats(status_codes, file_size)
    sys.exit(0)


# Handle Request Status Codes
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
file_size = 0

signal.signal(signal.SIGINT, signal_handler)

try:
    for i, line in enumerate(sys.stdin, 1):
        split_line = line.split()
        if len(split_line) < 2:
            continue
        if int(split_line[-2]) in status_codes:
            status_codes[int(split_line[-2])] += 1
        file_size += int(split_line[-1])
        if i % 10 == 0:
            print_stats(status_codes, file_size)
except KeyboardInterrupt:
    pass
finally:
    print_stats(status_codes, file_size)
