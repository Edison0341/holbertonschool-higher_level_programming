#!/usr/bin/python3
"""module for appending text to a file"""

def append_write(filename="", text=""):
    """appends the give text to a utf-8 text file"""

    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
