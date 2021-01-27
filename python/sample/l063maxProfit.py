#!/usr/bin/python
# coding=utf-8
# Copyright 2021 yaitza. All Rights Reserved.
#
#     https://yaitza.cn/
#
# My Code hope to usefull for you.
# ===================================================================

'''
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

 

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

限制：

0 <= 数组长度 <= 10^5
'''

def maxProfit(prices=list):
    """
    :type prices: List[int]
    :rtype: int
    """
    min_price = int(1e9)
    max_price = 0
    max_profit = 0
    for item in prices:
        max_profit = max(item - min_price, max_profit)
        min_price = min(item, min_price)
    return max_profit




print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
print(maxProfit([2,1,4]))