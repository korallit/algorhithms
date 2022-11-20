# coding: utf-8

import sys
from time import process_time


def compare_neighbours(items, index):
    prev = items[index-1]
    if prev > items[index]:
        items[index-1] = items[index]
        items[index] = prev


def greatest_to_end(items, length):
    for i in range(1, length):
        compare_neighbours(items, i)


def sort_super(items):
    for i in range(len(items), 0, -1):
        greatest_to_end(items, i)


def sort(items):
    for i in range(len(items), 0, -1):
        for ii in range(1, i):
            prev = items[ii-1]
            if prev > items[ii]:
                items[ii-1] = items[ii]
                items[ii] = prev


if __name__ == '__main__':
    # reading input
    sys.stdout.write("input list: ")
    sys.stdout.flush()
    input_data = sys.stdin.readline()
    data = [int(i.strip()) for i in input_data.split(',')]

    # processing while measuring time
    t1 = process_time()
    sort(data)
    t2 = process_time()

    # printing result
    msg = '\n'.join([
        f"result: {data}",
        f"process time: {t2 - t1}",
    ])
    print(msg)
