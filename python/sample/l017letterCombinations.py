#!/usr/bin/python
# coding=utf-8
# Copyright 2020 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

__author__ = "yaitza"
__date__ = "2020-12-18 14:31"

dict_digits_chars = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                     '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}


def letterCombinations(digits):
    if not digits:
        return list()

    combination = list()
    combinations = list()

    def backtrack(index):
        if index == len(digits):
            combinations.append("".join(combination))
        else:
            digit = digits[index]
            for letter in dict_digits_chars[digit]:
                combination.append(letter)
                backtrack(index+1)
                combination.pop()
    backtrack(0)

    return combinations

print(letterCombinations("232"))

