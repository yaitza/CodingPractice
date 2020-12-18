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

'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

 

示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 

提示：

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

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



