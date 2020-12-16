#!/usr/bin/python
# coding=utf-8
# Copyright 2020 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

__author__ = "yaitza"
__date__ = "2020-12-16 11:23"

INT_MIN = - 2 ** 31 
INT_MAX = 2 ** 31 - 1

table = {'start': ['start', 'signed', 'in_number', 'end'],
         'signed': ['end', 'end', 'in_number', 'end'],
         'in_number': ['end', 'end', 'in_number', 'end'],
         'end': ['end', 'end', 'end', 'end']}


def char_to_int(s):
    state = 'start'
    sign = 1
    ans = 0
    for c in s:
        state = table[state][get_col(c)]
        if state == 'in_number':
            ans = ans * 10 + int(c)
            ans = min(ans, INT_MAX) if sign == 1 else min(ans, -INT_MIN)
        if state == 'signed': 
            sign = 1 if c == '+' else -1
    return sign * ans


def get_col(c):
    if c.isspace():
        return 0
    elif c == '-' or c == '+':
        return 1
    elif c.isdigit():
        return 2
    else:
        return 3
