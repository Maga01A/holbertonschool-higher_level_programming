#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    count = len(argv) - 1
    if count == 0:
        print("0 argument(s).")
    else:
        print("{} argument(s):".format(count))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
