#!/usr/bin/python
# coding=utf-8
# Copyright 2020 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

__author__ = "yaitza"
__date__ = "2020-12-18 10:23"


def threeSumClosest(nums, target):
    sorted_nums = sorted(nums)
    # if abs(sorted_nums[0] - target) > 0:
    #     return sum(sorted_nums[0:3])

    length = len(sorted_nums)
    results = {}
    for i in range(length):
        now = sorted_nums[i]
        left = i + 1
        right = length - 1
        while left < right:
            delta = now + sorted_nums[left] + sorted_nums[right] - target
            if delta > 0:
                results[abs(delta)] = now + sorted_nums[left] + sorted_nums[right]
                right = right - 1
            elif delta < 0:
                results[abs(delta)] = now + sorted_nums[left] + sorted_nums[right]
                left = left + 1
            else:
                return now + sorted_nums[left] + sorted_nums[right]
    return results[sorted(results.keys())[0]]


print(threeSumClosest([-1,2,1,-4], 1))
print(threeSumClosest([1, 1, 1, 1], 0))
print(threeSumClosest([-100, -98, -2, -1], -101))



