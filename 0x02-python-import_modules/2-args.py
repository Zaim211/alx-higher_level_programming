#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = len(sys.argv) - 1

    if x == 0:
        print("{} argument:".format(x))
    elif x == 1:
        print("{} argument:".format(x))
    else:
        print("{} argument:".format(x))

    if x >= 1:
        x = 0
        for arg in sys.argv:
            if x != 0:
                print("{}: {}".format(x, arg))
            x += 1
