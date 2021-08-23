"""
    Advent of code 2020 - day5
"""

import unittest
import math


def my_find(target, min_val, max_val, upper, lower):
    start = [min_val, max_val]
    for index, letter in enumerate(target):
        if index < len(target) - 1:
            step = (start[1] + 1) / 2 if start[0] == 0 else math.ceil((start[1] - start[0]) / 2)
            if letter == upper:
                start[0] = start[0] + int(step)
            elif letter == lower:
                start[1] = start[1] - int(step)
        elif index == len(target) - 1:
            if letter == upper:
                return start[1]
            elif letter == lower:
                return start[0]


def get_row(code):
    """
        Size 7.
        Range: 0 - 127
        F - lower - [0, 63]
        B - upper - [64, 127]
    :param code:
    :return:
    """

    # 0, 127
    # |  lower | upper |
    # 0       63 64     127

    # --> B --> 64, 127    s: +64
    # --> F --> 64, 95     s: -32
    # --> F --> 64, 79     s: -16
    # --> F --> 64, 71     s: -8
    # --> B --> 68, 71     s: +4
    # --> B --> 70, 71    s: +2
    # --> F --> 70

    target = code[:7]
    start = [0, 127]
    return my_find(target, 0, 127, 'B', 'F')


def get_column(code):
    """
        L - means lower half.               [0,3]
        R - means to keep the upper half.   [4,7]
        Numbered 0 - 7
        Size: 3
    """
    target = code[-3:]
    return my_find(target, 0, 7, 'R', 'L')


def get_id(row, column):
    """ Multiply the row by 8, then add the column"""
    return row * 8 + column


def run(code):
    row = get_row(code)
    col = get_column(code)
    seat_id = get_id(row, col)
    return {'row': row, 'column': col, 'seat ID': seat_id}


import numpy


def read(file_name):
    results = []
    with open(file_name, "r") as d:
        for line in d:
            results.append(int(run(line.strip())['seat ID']))
    r = numpy.array(results, dtype=int)
    r.sort()
    print(r)


class Tests(unittest.TestCase):
    def test_run(self):
        res = run("FBFBBFFRLR")
        self.assertEqual(44, res['row'])
        self.assertEqual(5, res['column'])
        self.assertEqual(357, res['seat ID'])

        res = run("BFFFBBFRRR")
        self.assertEqual(70, res['row'])
        self.assertEqual(7, res['column'])
        self.assertEqual(567, res['seat ID'])

        res = run("FFFBBBFRRR")
        self.assertEqual(14, res['row'])
        self.assertEqual(7, res['column'])
        self.assertEqual(119, res['seat ID'])

        res = run("BBFFBBFRLL")
        self.assertEqual(102, res['row'])
        self.assertEqual(4, res['column'])
        self.assertEqual(820, res['seat ID'])


if __name__ == '__main__':
    # unittest.main()
    read('data.txt')
