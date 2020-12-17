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

'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) < 3:
        return []
    length = len(nums)
    result = []

    if length == 1 and nums[0] == 0:
        return result.append(nums)

    for i in range(length):
        for j in range(i + 1, length):
            third_num = -(nums[i] + nums[j])
            last_num = nums[j + 1:]
            if last_num.__contains__(third_num):
                tmp_result = sorted([nums[i], nums[j], third_num])
                if not result.__contains__(tmp_result):
                    result.append(tmp_result)
    return result


def threeSumEx(nums):
    if len(nums) < 3:
        return []
    length = len(nums)
    sort_nums = sorted(nums)

    result = []

    for i in range(len(sort_nums)):
        if sort_nums[i] > 0:
            return result

        if i > 0 and sort_nums[i] == sort_nums[i-1]:
            continue

        left = i + 1
        right = length - 1
        now = sort_nums[i]

        while left < right:
            if sort_nums[right] + sort_nums[left] > -now:
                right = right - 1
            elif sort_nums[right] + sort_nums[left] < -now:
                left = left + 1
            else:
                result.append([now, sort_nums[left], sort_nums[right]])
                while right > left and sort_nums[right] == sort_nums[right - 1]:
                    right = right - 1
                while right > left and sort_nums[left] == sort_nums[left + 1]:
                    left = left + 1

                left = left + 1
                right = right - 1

    return result
