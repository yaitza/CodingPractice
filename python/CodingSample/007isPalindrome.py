#!/usr/bin/python
# coding=utf-8
# Copyright 2020 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

__author__ = "yaitza"
__date__ = "2020-12-14 17:02"

'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def isPalindrome(intNo):
    intStr = str(intNo)
    n = len(intStr)
    result = True
    for i in range(int(n/2)):
        if intStr[i].__eq__(intStr[-(i+1)]):
            result = result and True
        else:
            result = result and False
    return result

def isPalindromeEx(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    revert_number = 0
    while x > revert_number:
        revert_number = revert_number * 10 + x % 10
        x = int(x / 10)

    if revert_number == x or int(revert_number / 10) == x:
        return True
    else:
        return False

print(isPalindromeEx(0))
print(isPalindromeEx(101))

print(isPalindromeEx(-121))
