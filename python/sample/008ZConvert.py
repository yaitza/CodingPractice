#!/usr/bin/python
# coding=utf-8
# Copyright 2020 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

__author__ = "yaitza"
__date__ = "2020-12-14 17:57"

'''
6. Z 字形变换
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
'''


def zconvert(s, numRows):
    if numRows == 1:
        return s

    middle = ["" for i in range(numRows)]
    director = True
    index = 0
    for i in range(len(s)):
        if i % (numRows - 1) == 0:
            director = not director
        middle[index] = middle[index] + s[i]
        if not director:
            index = index + 1
        else:
            index = index - 1

    result = ""
    for item in middle:
        result = result + item
    return result


print(zconvert("LEETCODEISHIRING", 4))
print(zconvert("LEETCODEISHIRING", 3))



