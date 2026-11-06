#!/usr/bin/python3
"""Module to convert Roman numerals to integers"""


def roman_to_int(roman_string):
    """Converts a roman numeral to an integer"""

    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    rom_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    length = len(roman_string)
    for i in range(length):
        if i < length - 1 and \
           rom_dict[roman_string[i]] < rom_dict[roman_string[i + 1]]:
            total -= rom_dict[roman_string[i]]
        else:
            total += rom_dict[roman_string[i]]

    return total
