#!/usr/bin/python
# coding=utf-8
# Copyright 2020 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

__author__ = "yaitza"
__date__ = "2020-12-31 13:56"

'''
剑指 Offer 57. 和为s的两个数字
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]
 

限制：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums) - 1

        while start < end:
            value_start = nums[start]
            value_end = nums[end]
            if value_start + value_end < target:
                start = start + 1

            if value_start + value_end > target:
                end = end - 1

            if value_start + value_end == target:
                return [value_start, value_end]
        return []


if __name__ == "__main__":
    ss = Solution()
    print(ss.twoSum([2, 7, 11, 15], 9))
    print(ss.twoSum([10, 26, 30, 31, 47, 60], 40))
    print(ss.lastRemaining(5, 3))