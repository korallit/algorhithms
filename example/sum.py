# coding: utf-8

import sys
from time import process_time


def my_sum(items):
    res = 0
    for i in items:
        if not isinstance(i, int):
            continue
        res += i
    return res


if __name__ == '__main__':
    # reading input
    sys.stdout.write("input list: ")
    sys.stdout.flush()
    input_data = sys.stdin.readline()
    data = [int(i.strip()) for i in input_data.split(',')]

    # processing while measuring time
    t1 = process_time()
    result = my_sum(data)
    t2 = process_time()

    # printing result
    msg = '\n'.join([
        f"result: {result}",
        f"process time: {t2 - t1}",
    ])
    print(msg)
