#!/usr/bin/python3
"""
Validate Dataset as UTF-8
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.
    """
    num_bytes = 0

    for num in data:
        # Get the 8 least significant bits of the integer
        byte = num & 0xFF
        # print(f"Num of Bytes: {num_bytes}")
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 7) == 0:
                # 1-byte character (ASCII)
                # print(f"Byte == 7: {num}, and {byte}")
                num_bytes = 0
            elif (byte >> 5) == 0b110:
                # print(f"Byte == 5: {num}, and {byte}")
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                # print(f"Byte == 4: {num}, and {byte}")
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                # print(f"Byte == 3: {num}, and {byte}")
                num_bytes = 3
            else:
                # print("#Print False ", num)
                return False
        else:
            # Check that the byte is a valid continuation byte
            if (byte >> 6) != 0b10:
                # print("#Print False2 ", num)
                return False
        # num_bytes -= 1

    return num_bytes == 0
