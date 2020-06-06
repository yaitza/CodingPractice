#!/usr/bin/python
# coding=utf-8
# Copyright 2020 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

__author__ = "yaitza"
__date__ = "2020-06-06 11:44"

' 测试数据 '
# data_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# data_array = [[1], [2], [3]]
# data_array = []
# data_array = [[1, 2, 3]]
# data_array = [[4, 5, 6], [7, 8, 9]]

# data_array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# data_array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]


def arrangement(array):
    """
    矩阵行列互换
    :param array: 传入矩阵(二维数组)
    :return: 返回
    """
    if array is None:
        return []
    # 列
    columns = array[0].__len__()
    # 行
    rows = array.__len__()

    if columns == 1 & rows == 1:
        return array[0]

    new_array = []
    for column in range(columns-1, -1, -1):
        new_row_array = []
        for row in range(rows):
            new_row_array.append(array[row][column])
        new_array.append(new_row_array)

    return new_array


def circle_show(data_array):
    """
    递归转换矩阵并返回
    :param data_array:
    :return: 矩阵顺时针显示数组
    """
    if not data_array:
        return []

    cor = data_array[0].__len__()
    ror = data_array.__len__()
    if cor == 1:
        result_array = []
        for i in range(ror):
            result_array.append(data_array[i][0])
        return result_array
    if ror == 1:
        result_array = []
        for i in range(cor):
            result_array.append(data_array[0][i])
        return result_array

    new_data_array = data_array[1:]
    co = new_data_array[0].__len__()
    ro = new_data_array.__len__()
    if co == 1:
        result_array = []
        for i in range(ro):
            result_array.append(new_data_array[i][0])
        result = result_array
    elif ro == 1:
        result_array = []
        for i in range(co-1, -1, -1):
            result_array.append(new_data_array[0][i])
        result = result_array
    else:
        results = arrangement(new_data_array)
        result = circle_show(results)
    return data_array[0] + result


def spiralOrder(data_array):
    """
    优秀实现
    :param data_array:
    :return:
    """
    return list(data_array[0]) + spiralOrder(list(zip(*data_array[1:]))[::-1]) if data_array else []


print(spiralOrder(data_array))
print(circle_show(data_array))



