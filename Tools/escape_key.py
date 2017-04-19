#!/usr/bin/env python

import sys


def escape_key(key):
    """Return the make command to call bootloader make."""
    text = 'AES_KEY=\\"'
    for i in range(0, len(key), 2):
        text += '\\\\x' + key[i] + key[i+1]
    text += '\\" make'
    return text


def main():
    if len(sys.argv) != 2:
        print("Usage: escape_key.py key")
        return 1

    print(escape_key(sys.argv[1]))


if __name__ == '__main__':
    main()

# vim :set ts=4 sw=4 sts=4
