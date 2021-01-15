#!/usr/bin/python
# coding=utf-8
# Copyright 2020 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

__author__ = "yaitza"
__date__ = "2021-01-14 14:23"

'''
剑指 Offer 42. 连续子数组的最大和
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

 

示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
 

提示：

1 <= arr.length <= 10^5
-100 <= arr[i] <= 100
'''


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[i] += max(nums[i-1], 0)
        return max(nums)

    def getMaxSubArray(self, nums):
        copynums = [item for item in nums]
        result = list()

        for i in range(1, len(nums)):
            if nums[i-1] < 0:

                result.clear()
            else:
                nums[i] = nums[i]+nums[i-1]

            result.append(copynums[i])

        return result


if __name__ == "__main__":
    ss = Solution()
    print(ss.maxSubArray([-2,1,-3,4,-1,2,1,-5,4,-6,1,4]))
    print(ss.getMaxSubArray([-2,1,-3,4,-1,2,1,-5,4,-6,1,4]))