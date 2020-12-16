#!/usr/bin/python
# coding=utf-8
# Copyright 2020 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

__author__ = "yaitza"
__date__ = "2020-12-16 18:01"


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    single_nums = list(set(nums))
    length = len(single_nums)
    results = []
    result = []
    flag = False


    for i in range(length):

        if len(result) < 4 and sum(result) == 0:
            result.append(nums[i])
            flag = True

        if flag:
            result.pop()
            flag = False


def get_not_repeat_arrangement(nums_list):
    if len(nums_list) <= 2:
        return nums_list

    result = []
    for i in range(len(nums_list)):
        middle = nums_list[:i] + nums_list[i+1:]
        all_case = get_not_repeat_arrangement(middle)
        for case in all_case:
            tmp = []
            tmp.append(nums_list[i])
            if not isinstance(case, list):
                tmp.append(case)
            else:
                tmp.extend(case)
            result.append(tmp)
    return result

print(get_not_repeat_arrangement([1, 2, 3, 4]))
