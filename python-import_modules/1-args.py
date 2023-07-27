#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    lists = sys.argv
    num = len(lists)

    if (num == 1):
            print("{} arguments." .format(num - 1))
    else:
        if (num == 2):
            print("{} argument:" .format(num - 1))
        else:
            print("{} arguments:" .format(num - 1))
        for i in range(1, num):
            print("{}: {}" .format(i, lists[i]))

