#!/usr/bin/python
# coding=utf-8
# Copyright 2020 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

__author__ = "yaitza"
__date__ = "2020-12-29 14:57"

'''
剑指 Offer 57 - II. 和为s的连续正数序列
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 

限制：

1 <= target <= 10^5
 
'''

class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        max_size = int(target/2) + 2
        middle_target = list(range(1, max_size))
        result = []
        middle_result = []

        while sum(middle_result) < target:
            if len(middle_target) == 0:
                break
            last_item = middle_target.pop()
            middle_result.append(last_item)
            if sum(middle_result) == target:
                max_size = max_size - 1
                middle_target = list(range(1, max_size))
                result.insert(0, sorted(middle_result))
                middle_result = []
            if sum(middle_result) > target:
                middle_result.pop(0)
                max_size = max_size - 1

        return result

if __name__ == "__main__":
    ss = Solution()
    print(ss.findContinuousSequence(9))
    print(ss.findContinuousSequence(15))










