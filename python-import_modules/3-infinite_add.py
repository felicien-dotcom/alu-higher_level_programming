#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    for arg in sys.argv[1:]:
        try:
        # Cast each argument to an integer and add to total
            total += int(arg)
        except ValueError:
        # Ignore non-integer arguments if any slip through
            pass
    print(total)
