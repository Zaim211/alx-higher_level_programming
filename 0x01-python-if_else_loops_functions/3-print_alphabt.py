#!/usr/bin/python3
for n in range(26):
    if n != 5 and n != 17:
        print("{:s}".format(chr(n + ord("a"))), end="")
