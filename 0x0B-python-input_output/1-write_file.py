#!/usr/bin/python3
"""
Contains the write_file function
"""


def write_file(filename="", text=""):
    """returns the number of chars written to "filename" from "text"""
    with open(filename, 'w', encouding="utf-8") as f:
        return f.write(text)
