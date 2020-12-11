#!/usr/bin/python
# coding=utf-8
# Copyright 2020 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

__author__ = "yaitza"
__date__ = "2020-12-11 9:33"

'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
给定一个 没有重复 数字的序列，返回其所有可能的全排列。例如：0-9个数字，返回大于2个数字的所有排列。
'''

result = set()


def Premutation(input):
    if len(input) <= 1:
        result.add(input)
        return input

    res = set()
    for i in range(len(input)):
        var = input[:i] + input[i+1:]
        all_case = Premutation(var)
        for item in all_case:
            r = input[i] + item
            if len(r) > 2:
                result.add(r)
            res.add(input[i] + item)
    return sorted(res)


alist = Premutation("abc")

print(alist)
print(result)