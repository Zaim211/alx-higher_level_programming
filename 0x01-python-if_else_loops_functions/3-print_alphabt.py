#!/usr/bin/python3
for n in range(26):
    if n != 4 and n != 16:
        print("{:s}".format(chr(n + ord("a"))), end="")
