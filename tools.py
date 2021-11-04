import sys
import time


def delay_print(s, t):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(t)


def clearScreen():
    for _ in range(0, 100):
        print("\n")

