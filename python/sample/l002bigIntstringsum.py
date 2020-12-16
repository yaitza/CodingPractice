#!/usr/bin/python
# coding=utf-8
# Copyright 2020 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

__author__ = "yaitza"
__date__ = "2020-06-11 11:00"


def big_int_str_sum(str1, str2):
    """
    大数据超长数据相加
    :param str1: 超长数字1
    :param str2: 超长数字2
    :return: 返回相加结果
    """
    results = []

    if not str1:
        return str2
    elif not str2:
        return str1
    else:
        if len(str1) > len(str2):
            results.extend(str1[:len(str1) - len(str2)])
            tmpstr1 = str1[len(str1) - len(str2):]
            temp = zip(tmpstr1[:], str2[:])
        elif len(str1) < len(str2):
            results.extend(str2[:len(str2) - len(str1)])
            tmpstr2 = str2[len(str2) - len(str1):]
            temp = zip(str1, tmpstr2)
        else:
            temp = zip(str1, str2)
        for s1, s2 in temp:
            results.append(int(s1) + int(s2))
    for item in range(len(results)-1, -1, -1):
        jinwei = int(results[item] / 10)
        yuanwei = results[item] % 10

        if item == 0 & jinwei > 0:
            results = [jinwei] + results
        else:
            results[item-1] = int(results[item-1]) + jinwei
        results[item] = yuanwei
    return results


str1 = "15523574574567456729"
str2 = "223546376898798555"

print(big_int_str_sum(str1, str2))

