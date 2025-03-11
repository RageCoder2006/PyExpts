import sys
import time


def rotating_line():
    symbols = ['|', '/', '-', '\\']
    while True:
        for symbol in symbols:
            sys.stdout.write('\r ' + symbol)
            sys.stdout.flush()
            time.sleep(0.2)


rotating_line()
