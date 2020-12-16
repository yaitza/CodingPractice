#!/usr/bin/python
# coding=utf-8
# Copyright 2020 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

__author__ = "yaitza"
__date__ = "2020-07-14 15:48"

'''
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
​
例如，给定三角形：
​
[
   [2],
  [3,4],
 [6,5,7],
[4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
​​
说明：
如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
'''




def triangle_min_path(s):
    """
    :param trianleArray: 三角形数组
    :return: 返回最小路径值
    """
    depth = s.__len__()
    dp = [[1e6]*depth for _ in range(depth)]

    for i in range(depth):
        for j in range(s[i].__len__()):
            if i == 0:
                dp[i][j] = s[i][j]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + s[i][j]
    result = dp[depth-1][0]
    for i in dp[depth-1]:
        if i < result:
            result = i
    return result

def get_minimum(x, array):
    if x + 1 == array.__len__():
        return array[x]
    else:
        return array[x+1] if array[x] > array[x+1] else array[x]


