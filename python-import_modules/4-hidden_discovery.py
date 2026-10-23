#!/usr/bin/python3
"""Module to find and print names defined inside hidden_4 module."""
import hidden_4
if __name__ == "__main__":
    names = dir(hidden_4)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
