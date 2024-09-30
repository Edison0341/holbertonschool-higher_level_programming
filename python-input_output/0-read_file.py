#!/usr/bin/python3
"""Reads a UTF-8 txt file"""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints it to stdout"""

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
