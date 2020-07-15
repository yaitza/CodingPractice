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


def triangle_min_path(trianleArray):
    """
    :param trianleArray: 三角形数组
    :return: 返回最小路径值
    """
    sum_array = []
    total = 0
    x_index = 0
    index_array = []
    for y in range(0, trianleArray.__len__()):
        x_array = []
        for x in range(0, trianleArray[y].__len__()):
            x_array.append(x)
        index_array.append(x_array)

    return sum


def get_minimum(x, array):
    if x + 1 == array.__len__():
        return array[x]
    else:
        return array[x+1] if array[x] > array[x+1] else array[x]

def test_get_minimum():
    assert get_minimum([1, 4, 5, 6]) == 1


def test_triangle_min_path():
    assert triangle_min_path([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 12
